#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/5/3 3:13 PM
# @Author  : Jerry
# @Desc    : 
# @File    : re_text.py


import re

HTML = '''
<!DOCTYPE html>
<!--[if IE 6]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 7]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 8]><html class="ie ie8"><![endif]-->
<!--[if IE 9]><html class="ie ie9"><![endif]-->
<!--[if !IE]><!--> <html> <!--<![endif]-->

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=no">

  <!-- Start of Baidu Transcode -->
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta name="applicable-device" content="pc,mobile">
  <meta name="MobileOptimized" content="width"/>
  <meta name="HandheldFriendly" content="true"/>
  <meta name="mobile-agent" content="format=html5;url=https://www.jianshu.com/p/8c1d1a38f9b9">
  <!-- End of Baidu Transcode -->

    <meta name="description"  content="re是正则的表达式,sub是substitute表示替换 re.sub是相对复杂点的替换 举个例子： inputs = &quot;hello 11 word 11&quot; 想11变成22 replacestr = inputs.replace(&quot;11&quot;,&quot;22) 但是如果是inputs = “hello 123 world 345” 想把数字都替换成222 就需要用正则替换 re.sub的参数：有五个参数...">

  <meta name="360-site-verification" content="604a14b53c6b871206001285921e81d8" />
  <meta property="wb:webmaster" content="294ec9de89e7fadb" />
  <meta property="qc:admins" content="104102651453316562112116375" />
  <meta property="qc:admins" content="11635613706305617" />
  <meta property="qc:admins" content="1163561616621163056375" />
  <meta name="google-site-verification" content="cV4-qkUJZR6gmFeajx_UyPe47GW9vY6cnCrYtCHYNh4" />
  <meta name="google-site-verification" content="HF7lfF8YEGs1qtCE-kPml8Z469e2RHhGajy6JPVy5XI" />
  <meta http-equiv="mobile-agent" content="format=html5; url=https://www.jianshu.com/p/8c1d1a38f9b9">

  <!-- Apple -->
  <meta name="apple-mobile-web-app-title" content="简书">

    <!--  Meta for Smart App Banner -->
  <meta name="apple-itunes-app" content="app-id=888237539, app-argument=jianshu://notes/27836454">
  <!-- End -->

  <!--  Meta for Twitter Card -->
  <meta content="summary" property="twitter:card">
  <meta content="@jianshucom" property="twitter:site">
  <meta content="re.sub的使用方法" property="twitter:title">
  <meta content="re是正则的表达式,sub是substitute表示替换 re.sub是相对复杂点的替换 举个例子： inputs = \&quot;hello 11 word 11\&quot; 想11变成22 ..." property="twitter:description">
  <meta content="https://www.jianshu.com/p/8c1d1a38f9b9" property="twitter:url">
  <!-- End -->

  <!--  Meta for OpenGraph -->
  <meta property="fb:app_id" content="865829053512461">
  <meta property="og:site_name" content="简书">
  <meta property="og:title" content="re.sub的使用方法">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://www.jianshu.com/p/8c1d1a38f9b9">
  <meta property="og:description" content="re是正则的表达式,sub是substitute表示替换 re.sub是相对复杂点的替换 举个例子： inputs = \&quot;hello 11 word 11\&quot; 想11变成22 replacestr...">
  <!-- End -->

  <!--  Meta for Facebook Applinks -->
  <meta property="al:ios:url" content="jianshu://notes/27836454" />
  <meta property="al:ios:app_store_id" content="888237539" />
  <meta property="al:ios:app_name" content="简书" />

  <meta property="al:android:url" content="jianshu://notes/27836454" />
  <meta property="al:android:package" content="com.jianshu.haruki" />
  <meta property="al:android:app_name" content="简书" />
  <!-- End -->


    <title>re.sub的使用方法 - 简书</title>

  <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="rlNnAgxSfaDxL3Wf4wl065dgjblVPxtc4XOOdFQMxNPjLomx+baZZh6KoS8QeDIkC8DQZ5wLLw45YMjV9jUmaw==" />

  <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web-d8f364aa94534f48835a.css" />
  
  <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-aa75deb505b1b600256a.css" />

  <link href="//cdn2.jianshu.io/assets/favicons/favicon-e743bfb1821442341c3ab15bdbe804f7ad97676bd07a770ccc9483473aa76f06.ico" rel="shortcut icon" type="image/x-icon">
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/57-a6f1f1ee62ace44f6dc2f6a08575abd3c3b163288881c78dd8d75247682a4b27.png" sizes="57x57" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/72-fb9834bcfce738fd7b9c5e31363e79443e09a81a8e931170b58bc815387c1562.png" sizes="72x72" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/76-49d88e539ff2489475d603994988d871219141ecaa0b1a7a9a1914f4fe3182d6.png" sizes="76x76" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/114-24252fe693524ed3a9d0905e49bff3cbd0228f25a320aa09053c2ebb4955de97.png" sizes="114x114" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/120-1bb7371f5e87f93ce780a5f1a05ff1b176828ee0d1d130e768575918a2e05834.png" sizes="120x120" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/152-bf209460fc1c17bfd3e2b84c8e758bc11ca3e570fd411c3bbd84149b97453b99.png" sizes="152x152" />

  <!-- Start of 访问统计 -->
    <script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "//hm.baidu.com/hm.js?0c0e9d9b1e7d617b3e6842e85b9fb068";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
  </script>

  <!-- End of 访问统计 -->
</head>

  <!-- 只给10%的用户添加代码 -->
  <!-- ###第四范式-智能推荐：代码直接复制 无需修改参数### -->
  <!-- ###功能：上报内容并反馈用户行为### -->
  <!--
  -->
  <body lang="zh-CN" class="reader-black-font">
    <!-- 全局顶部导航栏 -->
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
  <div class="width-limit">
    <!-- 左上方 Logo -->
    <a class="logo" href="/"><img src="//cdn2.jianshu.io/assets/web/nav-logo-4c7bbafe27adc892f3046e6978459bac.png" alt="Nav logo" /></a>

    <!-- 右上角 -->
      <!-- 未登录显示登录/注册/写文章 -->
      <a class="btn write-btn" target="_blank" href="/writer#/">
        <i class="iconfont ic-write"></i>写文章
</a>      <a class="btn sign-up" id="sign_up" href="/sign_up">注册</a>
      <a class="btn log-in" id="sign_in" href="/sign_in">登录</a>

    <!-- 如果用户登录，显示下拉菜单 -->

    <div id="navbar-jsds-enter">
    </div>

    <div id="view-mode-ctrl">
    </div>
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#menu" aria-expanded="false">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="menu">
        <ul class="nav navbar-nav">
            <li class="tab ">
              <a href="/">
                <span class="menu-text">首页</span><i class="iconfont ic-navigation-discover menu-icon"></i>
</a>            </li>
            <li class="tab ">
              <a id="web-nav-app-download-btn" class="app-download-btn" href="/apps?utm_medium=desktop&amp;utm_source=navbar-apps"><span class="menu-text">下载App</span><i class="iconfont ic-navigation-download menu-icon"></i></a>
            </li>
          <li class="search">
            <form target="_blank" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
              <input type="text" name="q" id="q" value="" autocomplete="off" placeholder="搜索" class="search-input" />
              <a class="search-btn" href="javascript:void(null)"><i class="iconfont ic-search"></i></a>
</form>          </li>
        </ul>
      </div>
    </div>
  </div>
</nav>

    
<div class="note">
  <div id="note-fixed-ad-container">
    <div id="fixed-ad-container">
      <div id="write-notes-ad"></div>
      <div id="youdao-fixed-ad"></div>
      <div id="yuxi-fixed-ad"></div>
      <div id="_so_pdsBy_0"></div>
    </div>
  </div>
  <div class="post">
    <div class="article">
        <h1 class="title">re.sub的使用方法</h1>

        <!-- 作者区域 -->
        <div class="author">
          <a class="avatar" href="/u/4b26c7f789d9">
            <img src="//cdn2.jianshu.io/assets/default_avatar/9-cceda3cf5072bcdd77e8ca4f21c40998.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" />
</a>          <div class="info">
            <span class="name"><a href="/u/4b26c7f789d9">潇湘demi</a></span>
            <!-- 关注用户按钮 -->
            <div props-data-classes="user-follow-button-header" data-author-follow-button></div>
            <!-- 文章数据信息 -->
            <div class="meta">
              <!-- 简书钻 -->
              <!-- 如果文章更新时间大于发布时间，那么使用 tooltip 显示更新时间 -->
                <span class="publish-time">2018.05.09 20:47</span>
              <span class="wordage">字数 494</span>
            </div>
          </div>
          <!-- 如果是当前作者，加入编辑按钮 -->
        </div>


        <!-- 文章内容 -->
        <div data-note-content class="show-content">
          <div class="show-content-free">
            <div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 320px;">
<div class="image-container-fill" style="padding-bottom: 43.01%;"></div>
<div class="image-view" data-width="744" data-height="320"><img data-original-src="//upload-images.jianshu.io/upload_images/10820970-3d0c8a3792147089.png" data-original-width="744" data-original-height="320" data-original-format="image/png" data-original-filesize="63432"></div>
</div>
<div class="image-caption"></div>
</div><p>re是正则的表达式,sub是substitute表示替换</p><p>re.sub是相对复杂点的替换</p><p>举个例子：</p><h2><br></h2><p>inputs = "hello 11 word 11"</p><p>想11变成22</p><p>replacestr = inputs.replace("11","22)</p><p>但是如果是inputs = “hello 123 world 345”</p><p>想把数字都替换成222</p><p>就需要用正则替换</p><p><b>re.sub的参数：</b><b>有五个参数</b></p><p>re.sub(pattern, repl, string, count=0, flags=0)</p><p>其中三个必选参数：pattern, repl, string</p><p>两个可选参数：count, flags</p><p><b>第一个：pattern</b></p><p>pattern，表示正则中的模式字符串。</p><p>反斜杠加数字（\N），则对应着匹配的组（matched group） </p><p>比如\6，表示匹配前面pattern中的第6个group </p><p><b>第二个参数：repl</b></p><p>repl，就是replacement，被替换，的字符串的意思。</p><p>repl可以是字符串，也可以是函数。</p><p>repl是字符串</p><p>如果repl是字符串的话，其中的任何反斜杠转义字符，都会被处理的。</p><p>即：</p><p>\n：会被处理为对应的换行符； </p><p>\r：会被处理为回车符； </p><p>其他不能识别的转移字符，则只是被识别为普通的字符： </p><p>比如\j，会被处理为j这个字母本身； </p><p>反斜杠加g以及中括号内一个名字，即：\g，对应着命了名的组，named group</p><p><b>第三个参数：string</b></p><p><b>string，即表示要被处理，要被替换的那个string字符串。<br></b></p><p>没什么特殊要说明。</p><p>第四个参数：count</p><p>举例说明：</p><p>继续之前的例子，假如对于匹配到的内容，只处理其中一部分。</p><p>比如对于：</p><p>hello 123 world 456 nihao 789</p><p>1</p><p>只是像要处理前面两个数字：123,456，分别给他们加111，而不处理789，</p><p>那么就可以写成：</p><p>replacedStr = re.sub("(?P\d+)", _add111, inputStr, 2);</p>
          </div>
        </div>
    </div>

    <!-- 如果是付费文章，未购买，则显示购买按钮 -->

    <!-- 连载目录项 -->

    <!-- 如果是付费文章 -->
      <!-- 如果是付费连载，已购买，且作者允许赞赏，则显示付费信息和赞赏 -->
        <div data-vcomp="free-reward-panel"></div>

      <div class="show-foot">
        <a class="notebook" href="/nb/25303416">
          <i class="iconfont ic-search-notebook"></i>
          <span>学习笔记</span>
</a>        <div class="copyright" data-toggle="tooltip" data-html="true" data-original-title="转载请联系作者获得授权，并标注“简书作者”。">
          © 著作权归作者所有
        </div>
        <div class="modal-wrap" data-report-note>
          <a id="report-modal">举报文章</a>
        </div>
      </div>

      <!-- 文章底部作者信息 -->
        <div class="follow-detail">
          <div class="info">
            <a class="avatar" href="/u/4b26c7f789d9">
              <img src="//cdn2.jianshu.io/assets/default_avatar/9-cceda3cf5072bcdd77e8ca4f21c40998.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" />
</a>            <div props-data-classes="user-follow-button-footer" data-author-follow-button></div>
            <a class="title" href="/u/4b26c7f789d9">潇湘demi</a>
          </div>
        </div>

    <div class="meta-bottom">
      <div class="btn like-group"></div>
      <div class="share-group">
        <a class="share-circle" data-action="weixin-share" data-toggle="tooltip" data-original-title="分享到微信">
          <i class="iconfont ic-wechat"></i>
        </a>
        <a class="share-circle" data-action="weibo-share" data-toggle="tooltip" href="javascript:void((function(s,d,e,r,l,p,t,z,c){var%20f=&#39;http://v.t.sina.com.cn/share/share.php?appkey=1881139527&#39;,u=z||d.location,p=[&#39;&amp;url=&#39;,e(u),&#39;&amp;title=&#39;,e(t||d.title),&#39;&amp;source=&#39;,e(r),&#39;&amp;sourceUrl=&#39;,e(l),&#39;&amp;content=&#39;,c||&#39;gb2312&#39;,&#39;&amp;pic=&#39;,e(p||&#39;&#39;)].join(&#39;&#39;);function%20a(){if(!window.open([f,p].join(&#39;&#39;),&#39;mb&#39;,[&#39;toolbar=0,status=0,resizable=1,width=440,height=430,left=&#39;,(s.width-440)/2,&#39;,top=&#39;,(s.height-430)/2].join(&#39;&#39;)))u.href=[f,p].join(&#39;&#39;);};if(/Firefox/.test(navigator.userAgent))setTimeout(a,0);else%20a();})(screen,document,encodeURIComponent,&#39;&#39;,&#39;&#39;,&#39;&#39;, &#39;推荐 潇湘demi 的文章《re.sub的使用方法》（ 分享自 @简书 ）&#39;,&#39;https://www.jianshu.com/p/8c1d1a38f9b9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=weibo&#39;,&#39;页面编码gb2312|utf-8默认gb2312&#39;));" data-original-title="分享到微博">
          <i class="iconfont ic-weibo"></i>
        </a>
        <a class="share-circle" data-toggle="tooltip"  id="longshare" target="_blank">
            <div class="qrcode" id="qrcode">
             <img src="//cdn2.jianshu.io/assets/web/download-index-side-qrcode-cb13fc9106a478795f8d10f9f632fccf.png" alt="Download index side qrcode" />
             <p>下载app生成长微博图片</p>
             </div>
          <i class="iconfont ic-picture"></i>
        </a>
        <a class="share-circle more-share" tabindex="0" data-toggle="popover" data-placement="top" data-html="true" data-trigger="focus" href="javascript:void(0);" data-content='
          <ul class="share-list">
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=&#39;+e(&#39;https://www.jianshu.com/p/8c1d1a38f9b9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=qzone&#39;)+&#39;&amp;title=&#39;+e(&#39;推荐 潇湘demi 的文章《re.sub的使用方法》&#39;),x=function(){if(!window.open(r,&#39;qzone&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-zone"></i><span>分享到QQ空间</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://twitter.com/share?url=&#39;+e(&#39;https://www.jianshu.com/p/8c1d1a38f9b9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=twitter&#39;)+&#39;&amp;text=&#39;+e(&#39;推荐 潇湘demi 的文章《re.sub的使用方法》（ 分享自 @jianshucom ）&#39;)+&#39;&amp;related=&#39;+e(&#39;jianshucom&#39;),x=function(){if(!window.open(r,&#39;twitter&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-twitter"></i><span>分享到Twitter</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://www.facebook.com/dialog/share?app_id=483126645039390&amp;display=popup&amp;href=https://www.jianshu.com/p/8c1d1a38f9b9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=facebook&#39;,x=function(){if(!window.open(r,&#39;facebook&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-facebook"></i><span>分享到Facebook</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://plus.google.com/share?url=&#39;+e(&#39;https://www.jianshu.com/p/8c1d1a38f9b9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=google_plus&#39;),x=function(){if(!window.open(r,&#39;google_plus&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-google"></i><span>分享到Google+</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,s1=window.getSelection,s2=d.getSelection,s3=d.selection,s=s1?s1():s2?s2():s3?s3.createRange().text:&#39;&#39;,r=&#39;http://www.douban.com/recommend/?url=&#39;+e(&#39;https://www.jianshu.com/p/8c1d1a38f9b9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=douban&#39;)+&#39;&amp;title=&#39;+e(&#39;re.sub的使用方法&#39;)+&#39;&amp;sel=&#39;+e(s)+&#39;&amp;v=1&#39;,x=function(){if(!window.open(r,&#39;douban&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r+&#39;&amp;r=1&#39;};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})()"><i class="social-icon-sprite social-icon-douban"></i><span>分享到豆瓣</span></a></li>
          </ul>
        '>更多分享</a>
      </div>
    </div>

        <a id="web-note-ad-1" target="_blank" href="/apps/redirect?utm_source=note-bottom-click"><img src="//cdn2.jianshu.io/assets/web/web-note-ad-1-c2e1746859dbf03abe49248893c9bea4.png" alt="Web note ad 1" /></a>

    <!--
    <div id="note-comment-above-ad-container">
      <span id="youdao-comment-ad" class="ad-badge">广告</span>
    </div>
    -->
    <div id="vue_comment"></div>
  </div>

  <div class="vue-side-tool" props-data-props-show-qr-code="0"></div>
</div>
<div class="note-bottom">
  <div class="js-included-collections"></div>
  <div data-vcomp="recommended-notes" data-lazy="1.5" data-note-id="27836454"></div>

  <!-- 相关文章 -->
      <!-- 未登录用户 -->
      <div class="seo-recommended-notes">

            <div class="note ">
                            <a class="title" target="_blank" href="/p/a567e6de717b?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Python正则表达式re模块手册</a>
              <p class="description">re模块手册    本模块提供了和Perl里的正则表达式类似的功能，不关是正则表达式本身还是被搜索的字符串，都可以是Unicode字符，这点不用担心，python会处理地和Ascii字符一样漂亮。 正则表达式使用反斜杆（\）来转义特殊字符，使其可以匹配字符本身，而不是指定其...</p>
              <a class="author" target="_blank" href="/u/324165d32970?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/6857392/4e5e5e58-5195-46d4-a834-bdce8af8cb2a.JPEG?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">喜欢吃栗子</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/147fab022566?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">细说python正则表达式</a>
              <p class="description">python的re模块--细说正则表达式 可能是东半球最详细最全面的re教程,翻译自官方文档,因为官方文档写的是真的好，所以，尽量保持原本的东西，做最少的改动，保持原汁原味！干货十足。如果能耐着性子看完，一定会感觉编程能力上一个新的档次！大家有空也可以到我的个人博客上看看 ...</p>
              <a class="author" target="_blank" href="/u/4d5ed5a5044e?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/6224338/be1540af-8def-4f91-ab7c-e9dfd76fa1ff.png?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">立而人</span>
</a>            </div>

            <div class="note have-img">
              <a class="cover" target="_blank" href="/p/135273d046f2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <img src="//upload-images.jianshu.io/upload_images/3672185-da6012a521392f5a.png?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>              <a class="title" target="_blank" href="/p/135273d046f2?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">编程语言对比系列：一、字符串的基本使用</a>
              <p class="description">前言 最先接触编程的知识是在大学里面，大学里面学了一些基础的知识，c语言，java语言，单片机的汇编语言等；大学毕业后就开始了app的开发之路，先使用oc进行iOS的app开发，后面应公司需求，又相继学习了java语言并使用java语言进行Android的app开发，后来微...</p>
              <a class="author" target="_blank" href="/u/6ffca93a395f?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/3672185/4a80ce6853d9.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">oceanfive</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/671670ff1e21?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Python中常用的re</a>
              <p class="description">re模块 开始使用re Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。 impo...</p>
              <a class="author" target="_blank" href="/u/47b2d5105e08?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//cdn2.jianshu.io/assets/default_avatar/12-aeeea4bedf10f2a12c0d50d626951489.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">Alex陌</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/9a7d0e28d151?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Python 正则表达式</a>
              <p class="description">简介正则表达式（regular expression）是可以匹配文本片段的模式。最简单的正则表达式就是普通字符串，可以匹配其自身。比如，正则表达式 ‘hello’ 可以匹配字符串 ‘hello’。要注意的是，正则表达式并不是一个程序，而是用于处理字符串的一种模式，如果你想用...</p>
              <a class="author" target="_blank" href="/u/adc9c8f3920d?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/5500696/3bd36d9f-524a-4756-a136-95c021f972bc.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">python红红</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/7060e84d3d2f?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">WebDriverException Cannot find firefox binary i...</a>
              <p class="description">最近在学习webdriver,顺便把遇到的问题记在这里，以便日后查阅，并分享给遇到相同问题的人。 问题：运行seleniumhq.org网站上的例子。 报如下错误 看这个报错应该是firefox安装路径不是默认路径。 解决方法：方法1、最简单的重新安装firefox到默认路...</p>
              <a class="author" target="_blank" href="/u/82f41ee3b584?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/2667804/fb88b448-1749-4940-a96e-949032a68e0e.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">七月尾巴_葵花</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/7d4b99bbb42b?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">第一篇</a>
              <p class="description">找一个自己写东西的地方 如果能有人看，那就再好不过啦 (๑`･ᴗ･´๑)</p>
              <a class="author" target="_blank" href="/u/a019b7064967?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/4726246/0b55c086d6e5.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">零点钟咖啡</span>
</a>            </div>

            <div class="note have-img">
              <a class="cover" target="_blank" href="/p/86cc1fd38b3c?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <img src="//upload-images.jianshu.io/upload_images/7355962-425b4fd52ac62e97.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>              <a class="title" target="_blank" href="/p/86cc1fd38b3c?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">左边阅读右边书法我叫读书笔记手帐1</a>
              <p class="description">进萌薇的第二期手帐班学习，回看了几次阅读笔记的讲课，似乎有所得。但我知道，没有得&quot;真经&quot;，原因一是囫囵吞枣，二是缺了点设计意识。 老师说，多做就好。 还真是。带着脑子多做同一件有点意思的事，总归还能捡到一点意趣。 以后小楷临习就直接写进手帐了。这是今天突然意识到的事。练习当...</p>
              <a class="author" target="_blank" href="/u/6d61bb97d105?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/7355962/2aaeb499-79e9-42e7-9ee6-7d8d0d97cb9f.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">孤山踏歌</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/d0caabafc258?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">[连载]晚安，少年:忧伤天使掉落人间10</a>
              <p class="description">1.要不表白？ “尹蔚然！你要是再乱说我就不理你了！” 他看我是真的生气了，走到我桌旁半蹲下，像是一只小猫一样央求着轻轻地摇摇我写字的胳膊。 “我错了好不好？” 我实在是生不起气来了。 “嗯。还有啊，换桌的事情必须得等到周考之后。” “好吧。”他撇撇嘴，像是赌气的小孩子。 ...</p>
              <a class="author" target="_blank" href="/u/3480256a2fbb?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/6845958/aa27dcdd-9bb7-48c3-8e7e-77a2fed99027.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">何悠</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/9f3aabf73a31?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">《肖生克的救赎》请给你自己不断创造新的希望</a>
              <p class="description">肖申克的救赎剧情介绍： 【剧情简介】： 《肖申克的救赎》(The Shawshank Redemption)改编自斯蒂芬·金《不同的季节》(Different Seasons)中收录的《丽塔海华丝及萧山克监狱的救赎》。影片《肖申克的救赎》在牢狱题材电影中突破了类型片的限制，...</p>
              <a class="author" target="_blank" href="/u/7e914f2d631d?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/3686886/8fd5b331-2e1c-45e6-b9d0-ff41d2839243.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">西西西小可爱</span>
</a>            </div>
      </div>
</div>

    <script type="application/json" data-name="page-data">{"user_signed_in":false,"locale":"zh-CN","os":"mac","read_mode":"day","read_font":"font2","note_show":{"is_author":false,"is_following_author":false,"is_liked_note":false,"follow_state":0,"uuid":"7d8449da-44c1-47b7-a9be-4898d61e8e26"},"note":{"id":27836454,"slug":"8c1d1a38f9b9","user_id":10820970,"notebook_id":25303416,"commentable":true,"likes_count":1,"views_count":8989,"public_wordage":494,"comments_count":1,"featured_comments_count":0,"total_rewards_count":0,"is_author":false,"paid_type":"free","paid":false,"paid_content_accessible":false,"author":{"nickname":"潇湘demi","total_wordage":1370,"followers_count":0,"total_likes_count":2}}}</script>
    
    <script src="//cdn2.jianshu.io/assets/babel-polyfill-d171e3dec4b6c15634dd.js" crossorigin="anonymous"></script>
    <script src="//cdn2.jianshu.io/assets/web-base-9ed51f9145bf1236a5c3.js" crossorigin="anonymous"></script>
<script src="//cdn2.jianshu.io/assets/web-68bee61802ce02137b79.js" crossorigin="anonymous"></script>
    
    <script src="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-db1f88d97afde313aa40.js" crossorigin="anonymous"></script>
    <script>
  (function(){
      var bp = document.createElement('script');
      var curProtocol = window.location.protocol.split(':')[0];
      if (curProtocol === 'https') {
          bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
      }
      else {
          bp.src = 'http://push.zhanzhang.baidu.com/push.js';
      }
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(bp, s);
  })();
</script>

  </body>
</html>
'''

HTML1 = '''
<script src="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-db1f88d97afde313aa40.js" 
crossorigin="anonymous">12313123123</script>123123123
'''


result = re.sub(r"(?si)<script.+?</script>|<!--.+?-->|<style.+?</style>|<[^>]+>|\s+", " ", HTML1)
# 把标签替换为空,
print result
