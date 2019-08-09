from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    
    rent_term = forms.CharField(widget=forms.RadioSelect(choices=(('장기(2주이상)','장기(2주이상)'),('단기(2주미만)','단기(2주미만)'))))
    room_type = forms.CharField(widget=forms.RadioSelect(choices=(('원룸','원룸'),('투룸','투룸'),('복층형 원룸','복층형 원룸'),('쓰리룸+','쓰리룸+'))))
    host_stuff = forms.CharField(widget=forms.RadioSelect(choices=(('있음','있음'),('없음','없음'))))
    parking = forms.CharField(widget=forms.RadioSelect(choices=(('있음','있음'),('없음','없음'))))
    pet = forms.CharField(widget=forms.RadioSelect(choices=(('가능','가능'),('불가능','불가능'))))
    elevator = forms.CharField(widget=forms.RadioSelect(choices=(('있음','있음'),('없음','없음'))))
    option = forms.CharField(widget=forms.RadioSelect(choices=(('에어컨','에어컨'),('냉장고','냉장고'),('세탁기','세탁기'),('책상','책상'),('침대','침대'),('침대','싱크대'))))

    class Meta:
        model = Room
        fields = ('intro','pub_date','confirmation','rent_term','start_date','end_date','price','floor','room_type','area','host_stuff','parking','pet','elevator','option','detail','main_img','other_img','room_img')

        def __init__(self, *args, **kwargs):
          super(RoomForm, self).__init__(*args, **kwargs)
          self.fields['file'].required = False

        widgets = {
            'intro': forms.TextInput(
                attrs={
                        'class': 'form-control',
                        'placeholder': '방 소개글을 작성해 주세요.',
                      }
            ),
            'pub_date': forms.DateInput(
                attrs={
                        'class': 'form-control',
                        'type':  'date',
                      }
            ),
             'rent_term': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'start_date': forms.DateInput(
                attrs={
                        'class': 'form-control',
                        'type':  'date',
                      }
            ),
             'end_date': forms.DateInput(
                attrs={
                        'class': 'form-control',
                        'type':  'date',
                      }
            ),
             'price': forms.TextInput(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'floor': forms.TextInput(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'room_type': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'area': forms.TextInput(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'host_stuff': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'parking': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
              'pet': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
              'elevator': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
              'option': forms.Select(
                attrs={
                        'class': 'form-control',

                      }
            ),
               'detail': forms.Textarea(
                attrs={
                        'class': 'form-control',
                        'rows': '5',
                      }
            ),
        }

        labels = {
                    'intro': '소개글',
                    'pub_date': '등록일',
                    'confirmation': '확인서',
                    'rent_term': '임대유형',
                    'start_date': '임대 시작 날짜',
                    'end_date': '임대 종료 날짜',
                    'price': '가격',
                    'floor': '층',
                    'room_type': '방 유형',
                    'area': '면적(평)',
                    'host_stuff': '집주인 짐',
                    'parking': '주차장',
                    'pet': '애완동물 동반',
                    'elevator': '엘리베이터',
                    'option': '옵션',
                    'detail': '상세소개',
                    'main_img': '대표 사진',
                    'other_img': '화장실, 주방 사진',
                    'room_img': '방별 사진',
                 }