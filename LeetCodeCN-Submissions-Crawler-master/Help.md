# 使用方法
1. clone或者download到本地
2. 安装依赖库 pip install -r requirements.txt
3. 配置config.json文件，用户名，密码，本地存储地址，时间控制（天）
4. python3 main.py


# 一些说明
1. 目前支持的语言有：{"cpp": ".cpp", "python3": ".py", "python": ".py", "mysql": ".sql", "golang": ".go", "java": ".java",
                   "c": ".c", "javascript": ".js", "php": ".php", "csharp": ".cs", "ruby": ".rb", "swift": ".swift",
                   "scala": ".scl", "kotlin": ".kt", "rust": ".rs"}

1. 由于力扣网站登录方式变动，需要解决登录无限失败的问题，小改了login函数
2. 更新ProblemList至题号1147， 新的题号需要在ProblemList里手动添加
3. 新增一个ProblemListGenerator函数，用于生成新的ProblemList
