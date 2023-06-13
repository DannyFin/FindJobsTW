from findJobs.FindJobs import Jobs
keyword = "ESG"
job = Jobs(keyword)
job.search_links(max_pages=1) #設定爬取的頁數，一頁20個
job.find_jobs()#找工作
job.save_jobs()#把找到的工作存成excel檔案
job.draw_box()
job.draw_density()
job.show(column = "all") #查看想統計的欄位，如果欄位名稱輸入"all"，會統計所有欄位，
#若要快速關閉視窗可按ctrl+w