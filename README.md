# RecPlatform
专门为推荐系统搭建的一个平台，基于tornado，python3

## 构建依赖
* tornado
* SQLAlchemy
* alembic
* restful api
* itsdangerous


## 目录框架
* alembic.ini alembic的配置文件
* migrations/ 数据库迁移脚本
  * env.py 每次执行alembic都会加载该文件，提供项目Sqlalchemy Model的连接
  * script.py.mako 迁移脚本生成模版
  * versions 存放生成的迁移脚本目录
* config.py 配置文件，定义开发和生成环境配置，使用环境变量ENV来选择（suprevisor的`environment`设置）
* statics/
  * db/ 数据库相关脚本
  * favicon.ico 
* app/ 用于存放应用
  * __init__.py  初始化应用，日志、数据库等
  * models/ 数据库ORM
  * handlers/ 请求处理
  * main/ 主程序
    * __init__.py 创建蓝本
    * errors.py 错误处理
    * forms.py
    * views.py  程序的路由
  * api_1_0/  REST Web服务
    * __init__.py 创建蓝本
    * modelName.py  具体模块
    * errors.py 错误处理
<!-- * venv/ 这里是开发所需要的python虚拟环境，用virtualenvwrapper管理后，该文件在$HOME/.virtualenv/下面 -->
<!-- * serverConfig/ 这里存放服务器配置时使用的nginx，uwsgi配置文件以及https证书 -->
* requirements.txt 项目所有依赖包 `pip freeze > requirements.txt`
* main.py 用于启动程序
* tests/  单元测试
  * __init__.py
  * test*.py

## 常用命令
### alembic
Alembic 是 Sqlalchemy 的作者实现的一个数据库版本化管理工具，它可以对基于Sqlalchemy的Model与数据库之间的历史关系进行版本化的维护。
1. 初始化alembic，创建alembic.ini及指定目录migrations
```bash
alembic init migrations
```
2. 创建数据库版本
```bash
alembic revision --autogenerate -m "my first commit"
```
3. 更新模型到数据库
```bash
alembic upgrade head
```
4. 版本管理
```bash
alembic history  # 查看提交过的版本
alembic downgrade -n    # 回退n个版本
alembic upgrade +n # 前进n个版本
```
