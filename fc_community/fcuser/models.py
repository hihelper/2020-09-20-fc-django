from django.db import models


# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    # 이 부분은 어드민 페이지 내부에서 각 데이터베이스 하나하나가 보여지는 문구를 정해주는 것이다. 이걸 설정 안하면 그냥 단순히 object01..02..03.. 식으로만 보일 뿐이다.
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'

        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
