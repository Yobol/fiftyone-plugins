# fiftyone-plugins

`FiftyOne` 提供了插件机制来扩展平台功能。

```
FiftyOne provides a powerful plugin framework that allows for extending and customizing the functionality of the tool to suit your specific needs.

With plugins, you can add new functionality to the FiftyOne App, create integrations with other tools and APIs, render custom panels, and add custom buttons to menus.
```

## 插件机制

### 工作原理

### 运行插件

准备环境：

```Shell
conda create fiftyone-plugin-official-hello-world python=3.10
conda activate fiftyone-plugin-official-hello-world
```

安装 `FiftyOne`：

```Shell
pip3 install fiftyone
```

使用终端命令安装 `FiftyOne` 插件：

```Shell
# 安装官方社区所有插件
fiftyone plugins download https://github.com/voxel51/fiftyone-plugins

# 安装官方社区指定插件，如 @voxel51/io
fiftyone plugins download \
    https://github.com/voxel51/fiftyone-plugins \
    --plugin-names @voxel51/io

# 安装开源社区任何插件
fiftyone plugins download https://github.com/path/to/repo
```

也可以使用 `Python SDK` 安装插件：

```Python
import fiftyone.plugins as fop

# Download plugin(s) from a GitHub repository
fop.download_plugin("https://github.com/<user>/<repo>[/tree/branch]")

# Download plugin(b) by specifying the GitHub repository details
fop.download_plugin("<user>/<repo>[/<ref>]")

# Download specific plugins from a GitHub repository
fop.download_plugin(url_or_gh_repo, plugin_names=["<name1>", "<name2>"])
```

启动 `FiftyOne`：

```Python
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")
session = fo.launch_app(dataset)
```

`PS:` 可以使用环境变量 `export FIFTYONE_PLUGINS_DIR=/path/to/your/plugins` 修改默认目录，使用 `fiftyone config plugins_dir` 命令查看当前目录。

#### 终端命令

> https://docs.voxel51.com/cli/index.html#fiftyone-plugins

常用命令：

```Shell
# Prints info about plugins that you've installed locally
# 可以看到插件安装的本地目录，如 /home/yobol/fiftyone/__plugins__/@voxel51/io
fiftyone plugins info <name>

# Prints info about operators and panels that you've installed locally.
fiftyone operators info <name>

# List all plugins you've downloaded
fiftyone plugins list

# List the available operators and panels
fiftyone operators list

# Disable a particular plugin
fiftyone plugins disable <name>

# Enable a particular plugin
fiftyone plugins enable <name>
```

#### 编程接口

> https://docs.voxel51.com/api/fiftyone.plugins.html

### 开发插件

## 插件列表

### 官方插件

`FiftyOne` 官方社区提供了很多有用的插件：[voxel51/fiftyone-plugins](https://github.com/voxel51/fiftyone-plugins)。

#### 示例插件

一些用于学习如何构建插件的示例：[Example Plugins](https://github.com/voxel51/fiftyone-plugins?tab=readme-ov-file#example-plugins)。

##### hello-world

> https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/hello-world

一个同时使用了 `JS` 和 `Python` 的示例项目：

- 使用 `JS` 构建 `Panel`（和 `Component`）；
- 使用 `Python` 构建了 `Operator`。

#### 核心插件

##### @voxel51/io

> https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/io



#### 三方插件

`FiftyOne` 周边社区也提供了很多有用的插件：[Community Plugins](https://github.com/voxel51/fiftyone-plugins?tab=readme-ov-file#community-plugins)

### 自制插件
