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
		<style>
	.p {
		padding: 30px;
		border: 1px solid #888;
		margin: 20px;
	}
</style>
<h1>文章列表</h1>
<div id="list">
	<!-- <?php if(is_array($posts)): foreach($posts as $key=>$v): ?><div class="p">
			<h4><a href="<?php echo U('Index/post', array('id'=>$v['id']));?>"><?php echo ($v["title"]); ?></a></h4>
			<p><?php echo (date('Y:m:d H:i:s', $v["timestamp"])); ?></p>
		</div><?php endforeach; endif; ?> -->

	<?php
 foreach ($posts as $k => $v) { echo '<div class="p">'; echo '<h4><a href="'.U('Index/post', array('id'=>$v['id'])).'">'.$v['title'].'</a></h4>'; echo '<p>'.date('Y:m:d H:i:s', $v['timestamp']).'</p>'; echo '</div>'; } ?>
</div>
	</div>	
	<footer>Copyright @ EasyBlog</footer>
</body>
</html>