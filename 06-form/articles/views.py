from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 특정 단일 게시글의 상세 페이지를 응답 (+ 단일 게시글 조회)
def detail(request, pk):
    # pk로 들어온 정수 값을 활용 해 DB에 id(pk)가 pk인 게시글을 조회 요청 
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# 게시글을 작성하기 위한 페이지를 제공하는 함수
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html',context)


# 사용자로부터 데이터를 받아 저장하고 저장이 완료되었다는 페이지를 제공하는 함수
def create(request):
    # 요청 메서드가 POST라면
    if request.method == 'POST':
        #1.1 사용자로부터 받은 데이터를 인자로 통째로 넣어서 form인스턴스생성
        form = ArticleForm(request.POST)
        #1.2 유효성 검사
        if form.is_valid():
            #1.3 유효성 검사가 통과한다면 저장
            article = form.save()
            #1.4 상세 페이지로 리다이렉트
            return redirect('articles:detail',article.pk)
    # 2 POST 아니라면
    else:
        # 2.1 ArticleForm 인스턴스 생성
        form = ArticleForm()
    # case 1 : 1.2에서 내려왔을때: 실패하고 내려왔기 때문에 에러메세지 담은 form
    # case 2 : 2.1이 끝나고 내려왔을 때, 빈 form
    context = {
        'form': form,
    }

    return render(request,'articles/create.html',context)
    # 사용자로 부터 받은 데이터를 추출
    

    # DB에 저장 요청 (3가지 방법)
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 2.
    
    
    
    # 3.
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    # return redirect('articles:index')
    


def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # DB에 삭제 요청
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     # 몇번 게시글 정보를 보여줄지 조회
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article) # instance라는 인자가 update에필요
#     context = {
#         'article': article,
#         'form' : form
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     # 어떤 글을 수정하는지 먼저 조회
#     article = Article.objects.get(pk=pk)
   
#     form = ArticleForm(request.POST, instance=article) # 업데이트와 크리에이트의 구조가비슷
#     # 저장이냐 수정이냐를 판단하기위한 instance키워드 

#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request,'articles/edit.html', context)


# new와 create view의 공통점: 목적은 데이터생성으로 같다
# 차이점: new에는 조회(get)요청만 옴/ create는 form을통해서 POST요청만 온다
# 게시글 생성이고 데이터베이스 조작이니까

def update(request,pk):
    article = Article.objects.get(pk=pk)
    
    # 저장이냐 수정이냐를 판단하기위한 instance키워드 

   
        
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # 업데이트와 크리에이트의 구조가비슷
        if form.is_valid():
             form.save()
             return redirect('articles:detail', article.pk)
       
    else:
        form = ArticleForm(instance=article) # instance라는 인자가 update에필요
    context = {
        'article': article,
        'form' : form
    }
    return render(request,'articles/update.html', context)