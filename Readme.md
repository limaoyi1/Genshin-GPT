## 🎨 部署指南

> 项目运行需要python环境 ，推荐python3以上，作者使用的是python3.9

> 1. 创建虚拟环境

```bash
   python -m venv venv
```

> 2. 设置环境变量
```bash
   setx OPENAI_API_BASE "your url"
   setx OPENAI_API_KEY "your key"
```

> 2. 激活虚拟环境

```bash
   . venv/bin/activate
```

> 3. 安装要求的python组件

```bash
pip install -r requirements.txt
```

> 4. 在 config.ini 添加你的api key

> 5. 将 ./templates/index.html 中的 www.limaoyi.top 替换为 127.0.0.1

> 6. 运行项目

> 运行
```bash
python application.py
```

> 或者 (生产模式) 需要在 类linux 环境运行以下命令

```bash
gunicorn -b 0.0.0.0:5000 --log-level=debug --threads 4 app:application > gunicorn.log 2>&1 &
```

> 7. 访问 http://127.0.0.1:5000


# 运行gunicorn
gunicorn -b 0.0.0.0:4397 --log-level=info --threads 1 wsgi:application > gunicorn.log 2>&1 &