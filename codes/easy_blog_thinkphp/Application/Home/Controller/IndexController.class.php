<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
    	// 首页
    	$this->display();
    }

    public function list(){
    	// 文章列表页
        $posts = M('post')->select();
        $this->posts = $posts;
    	$this->display();
    }

    public function post(){
    	// 文章详情页
    	$id = I('id');
    	$post = M('post')->where(array(
    		'id' => $id
    		))->find();

    	// 将数据传递给$this对象
    	$this->post = $post;
    	$this->display();
    }

    public function handle(){
    	// 处理文章提交
    	$title = I('title');
    	$content = I('content');
    	$id = M('post')->data(array(
    		'title' => $title, 
    		'content' => $content,
    		'timestamp' => time()
    		))->add();
    	$this->redirect('Index/post', array('id' => $id));
    }
}