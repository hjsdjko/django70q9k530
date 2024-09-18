<template>
	<div style="height: 100%;">
		<el-main :style='"vertical" == "vertical" ? (2 == 1 ? {"minHeight":"100%","padding":"0","margin":"0 0 0 210px","position":"relative","display":"block"} : (2 == 2 ? (isCollapse ? {"minHeight":"100%","padding":"0 0 0 0px","margin":"0","position":"relative","background":"#f1f2f7","display":"block"} : {"minHeight":"100%","padding":"0 0 0 230px","margin":"0","position":"relative","background":"#f0f3f4","display":"block"}) : "")) : {"minHeight":"100%","margin":"0","position":"relative"}'>
			<!-- top -->
			<index-header :style='{"padding":"0 20px 0 20px","boxShadow":"0 1px 0px rgba(0,0,0,0.12), 0 1px 1px rgba(0,0,0,0.24)","margin":"0 auto","borderColor":"rgba(126, 96, 16, .2)","alignItems":"center","color":"#fff","display":"flex","justifyContent":"flex-end","top":"0","left":"0","background":"#2196F3","borderWidth":"0 0 0px","width":"calc(100% - 0px)","fontSize":"14px","position":"fixed","borderStyle":"solid","zIndex":"1000","height":"60px"}'></index-header>
			
			<!-- menu -->
			<template v-if="'vertical' == 'vertical'">
			  <template v-if="2 == 1">
				<index-aside :style='{"boxShadow":"1px 0 6px  rgba(64, 158, 255, .3)","overflow":"hidden","top":"0","left":"0","background":"#304156","bottom":"0","width":"210px","fontSize":"0px","position":"fixed","height":"100%","zIndex":"1001"}'></index-aside>
			  </template>
			  <template v-if="2 == 2">
				<index-aside :is-collapse="isCollapse" @oncollapsechange="collapseChange" :style='isCollapse ? {"boxShadow":"0px 0 0px rgba(255,205,155,1)","padding":"0px 0 0","borderColor":"rgba(126, 96, 16, .2)","bottom":"0","transition":"width 0.3s","overflow":"hidden","top":"0","left":"0","background":"#fff","borderWidth":"0 0px 0 0","width":"0px","fontSize":"0px","position":"fixed","borderStyle":"solid","height":"100%","zIndex":"1001"} : {"boxShadow":"0 2px 5px 0 rgba(239, 235, 235, 0.16), 0 2px 10px 0 rgba(72, 70, 70, 0.12)","padding":"80px 0","borderColor":"#096ab7","bottom":"0","transition":"width 0.3s","overflow":"hidden","top":"60px","left":"0","background":"url(http://codegen.caihongy.cn/20231022/fccea8193b004d42b1db87f0df4f86a4.png) no-repeat center top / 100% auto,#fff","borderWidth":"1px 0 0","width":"230px","fontSize":"16px","position":"fixed","borderStyle":"solid","height":"100%","zIndex":"1001"}'></index-aside>
			  </template>
			</template>
			<template v-if="'vertical' == 'horizontal'">
			  <template v-if="2 == 1">
				<index-aside :style='{"width":"100%","borderColor":"#efefef","borderStyle":"solid","background":"#304156","borderWidth":"0 0 1px 0","height":"auto"}'></index-aside>
			  </template>
			  <template v-if="2 == 2">
				<index-aside :style='{"borderColor":"#efefef","background":"#FFF","borderWidth":"0 0 1px 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}'></index-aside>
			  </template>
			</template>
			
			<!-- breadcrumb -->
			<bread-crumbs :title="title" :style='{"padding":"30px 30px","margin":"60px auto 0","borderColor":"#aaaaac","borderWidth":"0 0 1px","background":"#fff","display":"block","width":"100%","fontSize":"13px","borderStyle":"solid","zIndex":"9"}' class="bread-crumbs"></bread-crumbs>
			
			<!-- TagsView -->
			<tags-view />
			
			<router-view class="router-view"></router-view>
		</el-main>
	</div>
</template>

<script>
	import IndexAside from '@/components/index/IndexAsideStatic'
	import IndexHeader from '@/components/index/IndexHeader'
	import TagsView from '@/components/index/TagsView'
	import menu from "@/utils/menu";
	export default {
		components: {
			IndexAside,
			IndexHeader,
			TagsView
		},
		data() {
			return {
				menuList: [],
				role: "",
				currentIndex: -2,
				itemMenu: [],
				title: '',
				isCollapse: false,
			};
		},
		mounted() {
			let menus = menu.list();
			this.menuList = menus;
			this.role = this.$storage.get("role");
		},
		created() {
			this.init();
		},
		methods: {
			init(){
				this.$nextTick(()=>{
					
				})
			},
			collapseChange(collapse) {
				this.isCollapse = collapse
			},
			menuHandler(menu) {
				this.$router.push({
					name: menu.tableName
				});
				this.title = menu.menu;
			},
			titleChange(index, menus) {
				this.currentIndex = index
				this.itemMenu = menus;
			},
			homeChange(index) {
				this.itemMenu = [];
				this.title = ""
				this.currentIndex = index
				this.$router.push({
					name: 'home'
				});
			},
			centerChange(index) {
				this.itemMenu = [{
					"buttons": ["新增", "查看", "修改", "删除"],
					"menu": "修改密码",
					"tableName": "updatePassword"
				}, {
					"buttons": ["新增", "查看", "修改", "删除"],
					"menu": "个人信息",
					"tableName": "center"
				}];
				this.title = ""
				this.currentIndex = index
				this.$router.push({
					name: 'home'
				});
				
			}
		}
	};
</script>
<style lang="scss" scoped>
	a {
		text-decoration: none;
		color: #555;
	}

	a:hover {
		background: #00c292;
	}
	
	.el-main {
		padding: 0;
		display: block;
	}

	.nav-list {
		width: 100%;
		margin: 0 auto;
		text-align: left;
		margin-top: 20px;

		.nav-title {
			display: inline-block;
			font-size: 15px;
			color: #333;
			padding: 15px 25px;
			border: none;
		}

		.nav-title.active {
			color: #555;
			cursor: default;
			background-color: #fff;
		}
	}

	.nav-item {
		margin-top: 20px;
		background: #FFFFFF;
		padding: 15px 0;

		.menu {
			padding: 15px 25px;
		}
	}
	
	.detail-form-content {
	    background: transparent;
	}
</style>
