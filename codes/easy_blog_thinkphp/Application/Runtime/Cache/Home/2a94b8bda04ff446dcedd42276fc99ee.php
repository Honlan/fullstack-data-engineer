<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>我的博客</title>
</head>
<style>
	html, body {
		margin: 0;
		padding: 0;
	}
	header, footer {
		padding: 30px 40px;
		background-color: #f2f2f2;
		color: #666;
	}
	header a {
		padding: 0 20px;
		color: #999;
		text-decoration: none;
	}
	header a:hover {
		color: #333;
	}
	footer {
		text-align: center;
	}
	#content {
		padding: 30px 40px;
	} 
</style>
<body>
	<header>
		<a href="<?php echo U('Index/index');?>">首页</a>
		<a href="<?php echo U('Index/list');?>">文章列表</a>
	</header>
	<div id="content">
		<h1>欢迎来到我的博客</h1>

<form action="<?php echo U('Index/handle');?>" type="post">
	<h4>添加文章</h4>
	<input type="text" name="title" placeholder="标题">
	<textarea name="content" cols="30" rows="10" placeholder="内容"></textarea>
	<button type="submit">提交</button>
</form>
	</div>	
	<footer>Copyright @ EasyBlog</footer>
</body>
</html>