from django.db import models

# 自定义模型管理类
class BookInfoManager(models.Manager):

    # 默认查询未删除的图书信息
    # 调用父类的成员语法为：super().方法名
    def all(self):
        return super().all().filter(isDelete=0)

    def create_book(self, title, bpub_date):
        # 获取 self 所在的模型类。self此时表示实例化对象 objects ,objects所在的模型类就是 BookInfo，所以model_class此时指向的就是 BookInfo。
        # 使用此方法可以避免因模型类修改名称而导致的实例化找不到类对象的问题
        model_class = self.model
        # 创建实例对象
        book = model_class()
        # book = BookInfo()
        book.btitle = title
        book.bpub_date = bpub_date
        book.bread = 0
        book.bcomment = 0
        book.isDelete = 0
        book.save()

# 定义书籍模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)    # 书籍名称
    bpub_date = models.DateField()              # 发布日期
    bread = models.IntegerField(default=0)      # 阅读量
    bcomment = models.IntegerField(default=0)   # 评论量
    isDelete = models.BooleanField(default=False)   # 逻辑删除
    # 自定义模型管理器
    objects = BookInfoManager()

    class Meta:
        db_table = 'bookinfo'

    @classmethod
    def cls_create_book(cls, title, bpub_date):
        # cls 此时代表的是 BookInfo 这个类，book=cls() 也就是 book=BookInfo()
        book = cls()
        book.btitle = title
        book.bpub_date = bpub_date
        book.bread = 0
        book.bcomment = 0
        book.isDelete = 0
        book.save()

# 定义英雄模型类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)     # 英雄姓名
    hgender = models.BooleanField(default=True)     # 英雄性别，True为男
    hcomment = models.CharField(max_length=200)     # 英雄描述信息
    hbook = models.ForeignKey(BookInfo, on_delete=models.DO_NOTHING)       # 英雄与书籍关系为一对多