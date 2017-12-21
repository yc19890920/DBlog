# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from app.blog.choices import STATUS_CHOICES
from django.utils.encoding import smart_str

class Tag(models.Model):
    """ tag(标签云)对应的数据库
    """
    name = models.CharField(u'标签名', max_length=20)
    created = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        db_table = 'blog_tag'

    def __str__(self):
        return smart_str(self.name)

    __repr__ = __str__

class Category(models.Model):
    """ 另外一个表,储存文章的分类信息
    文章表的外键指向
    """
    name = models.CharField(u'类名', max_length=20)
    created = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        db_table = 'blog_category'

    def __str__(self):
        return smart_str(self.name)

    __repr__ = __str__

class Article(models.Model):

    title = models.CharField(u'标题', max_length=100, null=False, blank=False, db_index=True)
    content = models.TextField(u'正文', null=False, blank=False)
    status = models.CharField(u'文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.TextField(u'摘要', blank=True, null=True, help_text=u"可选项，若为空则摘取正文钱54个字符")
    views = models.PositiveIntegerField(u'阅读量', default=0)
    likes = models.PositiveIntegerField(u'点赞数', default=0)
    topped = models.BooleanField(u'置顶', default=False)
    auth = models.CharField(u"作者", max_length=50, null=False, blank=False)
    source = models.CharField(u"来源", max_length=50, null=True, blank=True)
    # 目录分类
    # on_delete 当指向的表被删除时，将该项设为空
    category = models.ForeignKey(Category, verbose_name=u'分类', null=True, on_delete=models.SET_NULL)
    # 标签云
    """
    ManyToManyField.related_name¶
        Same as ForeignKey.related_name.

    ManyToManyField.related_query_name¶
        Same as ForeignKey.related_query_name.

    ManyToManyField.limit_choices_to¶
        Same as ForeignKey.limit_choices_to.

    ManyToManyField.through¶
    Django will automatically generate a table to manage many-to-many relationships.
    However, if you want to manually specify the intermediary table,
     you can use the through option to specify the Django model that represents the intermediate table that you want to use.
    """
    tags = models.ManyToManyField(
        Tag,
        verbose_name=u'标签集合',
        blank=True,
        related_name="tag_set",        #  比如 得到一个Tag模型tag， 查询 tag.tag_set.all()
        related_query_name="article",  #
        through='ArticleTags',
        # through_fields=('article', 'tag'),
        help_text=u"文章标签，多选"
    )

    # auto_now_add : 创建时间戳，不会被覆盖
    created = models.DateTimeField(u'创建时间', auto_now_add=True)
    # auto_now: 自动将当前时间覆盖之前时间
    updated = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        db_table = 'blog_article'
        # Meta 包含一系列选项，这里的ordering表示排序, - 表示逆序
        # 即当从数据库中取出文章时，以文章最后修改时间逆向排序
        ordering = ['-updated']

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'article_id': self.pk})

    @property
    def topped_display(self):
        return u"是" if self.topped else u"否"

    @property
    def get_tags(self):
        return self.tags.all()

    @property
    def get_refer_ids(self):
        # tag_ids = self.tags.all().values_list("id", flat=True)
        tag_ids = ArticleTags.objects.filter(article=self).values_list("tag_id", flat=True)
        article_ids = ArticleTags.objects.filter(tag_id__in=tag_ids).values_list("article_id", flat=True)
        return article_ids

    def __str__(self):
        return smart_str(self.title)

    __repr__ = __str__


class ArticleTags(models.Model):
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tag)

    class Meta:
        auto_created = True
        db_table = 'blog_article_tags'

class BlogComment(models.Model):
    username = models.CharField(u'你的名称', max_length=100)
    email = models.CharField(u"你的邮箱", max_length=100)
    content = models.TextField(u'评论内容')
    created = models.DateTimeField(u'创建时间', auto_now_add=True)
    article = models.ForeignKey(Article, verbose_name=u'评论所属文章', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_comment'

    def __str__(self):
        return self.content[:20]


class Suggest(models.Model):
    """ 意见存储
    """
    username = models.CharField(u'你的名称', max_length=100)
    email = models.CharField(u"你的邮箱", max_length=100)
    content = models.TextField(u'建议', max_length=200)
    created = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        db_table = 'blog_suggest'

    def __str__(self):
        return smart_str(self.content)
