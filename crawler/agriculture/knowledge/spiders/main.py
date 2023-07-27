# 命令行运行
from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', 'filmspider'])
# cmdline.execute(cmd_line_str.split())

# vscode需要切换路径才能执行
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

cmd_parm = 'knowledgespider -o arg_kg.csv'
cmd_line_str = "scrapy crawl {0}".format(cmd_parm)
cmdline.execute(cmd_line_str.split())
# cmdline.execute(['scrapy', 'crawl', 'knowledgespider'])