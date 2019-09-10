# -*- coding: utf-8 -*-
import scrapy
from  postBar.items import PostbarItem

class BaidubaSpider(scrapy.Spider):
    name = 'baiduba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=网络安全&ie=utf-8&pn=9100']

    def parse(self, response):
        for i in range(1,20):     #　循环爬取只爬取前２０页
            print(response.status)
            lis = response.xpath("//*[@id='thread_list']/li")
            crs = lis.css("div > div.col2_right.j_threadlist_li_right > div.threadlist_lz.clearfix > div.threadlist_title.pull_left.j_th_tit > a")
            urls = crs.xpath("@href").extract()   # 获取爬取到每一个贴子的链接
            for u in urls:
                curl = "http://tieba.baidu.com"+u
                yield response.follow(curl,self.parseDetail)  # 打开详情页 准备爬取 内容 作者 回帖数量 以及标题
                trga = response.css("#frs_list_pager > a.next.pagination-item")[0]
                h = trga.xpath("@href")
                if len(h) > 0 :
                    nxturl = "https:"+h[0].extract()
                    yield  response.follow(nxturl,self.parse)





    def parseDetail(self,response):
        print("打开详情页:",response.url)
        title =response.css("#j_core_title_wrap > div.core_title.core_title_theme_bright > h1::text").extract_first()   # 根据css 样式爬取获得标题
        author = response.css("#j_p_postlist > div.l_post.j_l_post.l_post_bright.noborder > div.d_author > ul > li.d_name > a::text").extract_first() # 根据css 样式爬取到作者
        nums=response.css("#thread_theme_5 > div.l_thread_info > ul > li:nth-child(2) > span:nth-child(1)::text").extract()  # 根据 css 样式爬取到 回帖数量
        div_list=response.css("#j_p_postlist > div > div.d_post_content_main.d_post_content_firstfloor")  # 获得内容的整体
        it = PostbarItem()     # 创建item 然后把字段保存起来
        it["url"] = response.url
        it["title"] = title
        it["author"] = author
        it["nums"] = nums
        for div in div_list:
            connect =div.xpath("normalize-space(//div[@class='d_post_content j_d_post_content  clearfix']/text())").extract_first() # 获取到内容
            it["connect"]=connect
        yield  it   # 最后返回，循环爬取
