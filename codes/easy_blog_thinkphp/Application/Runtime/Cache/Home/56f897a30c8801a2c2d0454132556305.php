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
		<h1>文章内容</h1>
<h4><?php echo ($post["title"]); ?></h4>
<h5><?php echo (date('Y:m:d H:i:s', $post["timestamp"])); ?></h5>
<p><?php echo ($post["content"]); ?></p>

	</div>	
	<footer>Copyright @ EasyBlog</footer>
</body>
</html>