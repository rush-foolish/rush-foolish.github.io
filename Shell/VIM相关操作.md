### VIM相关操作

#### VIM/VI中的基本操作

**1.插入命令**

i: 在光标前插入, I: 在光标所在行的行首插入
a:在光标后插入, A:在光标所在行行尾插入
o:在光标所在行上插入新行，O:在光标所在行下插入新行

**2.光标移动命令**

h:光标左移, j:光标下移, k:光标上移, l:光标右移动
H:光标定位到屏幕最上面一行, M:光标移动到屏幕中央, L:光标移动到屏幕最下方
0: 光标移动到行首, $光标移动到行尾

**3.定位命令**

gg:回到文件首行, G:回到文件尾行
:n和nG: 光标定位到文件第n行(:20或20G表示光标定位到第20行)
:set nu 或:set number显示行号, :set nonu 取消显示行号

**4.删除命令**

x : 删除光标所在字符, nx:删除光标后n个字符
dd:删除光标所在行，ndd:删除光标所在行以后的n行
D:删除光标到行尾的内容
dG:删除光标所在行到文件末尾的内容
:n1,n2d:删除行n1到行n2的内容，包括第n1和n2行都被删除

**5.复制剪切粘贴命令**

yy 或 Y: 复制当前行
nyy或nY:从当前行开始赋值n行
剪切使用dd和ndd，相当于删除
p:在光标所在行之后粘贴
P:在光标所在行之前粘贴

**6.搜索和替换命令**

 命令模式下键入:/taret, 查找文件中所有的target串，n:下一个target出现的地方(从前往后), N:下一个target出现的地方(从后往前)

:set ic :搜索忽略大小写
:%s/old/new/g 将全部old替换为new, 不许确认直接替换
:n1,n2s/old/new/g 将n1-n2行中出现的所有old替换为new, 不需确认直接替换
:u 撤销
:redo 恢复

**若将上述命令中的g变为c则是需要逐条确认的替换**

#### VIM的几种模式

1. Normal Mode(默认进入vim，进入该模式)

2. Visual Mode（可视化模式，按下<ESC>+v/ctrl-v，该模式下选定一些字符、行、列。
	- 删除：光标所在位置，进入可视模式，移动上下左右键，选中内容，按d
	- 多列插入：按以上选中内容，按下shift-i，光标回到起始位置，键入内容
	- 复制：选中内容后按 y,选中全文内容（<esc>ggVG

3. Insert Mode (i进入插入模式)

4. Select Mode (普通模式，按下gh进入)

5. Command-Line/Ex Mode (<ESC>+ :进入，可以设置vim当前的格式)
	－ echo $VIM:显示vimrc所在路径
	－ echo $PATH:显示当前文件路径

6. Paste Mode(粘贴模式，复制的代码粘贴时不受vim设置的格式影响)

#### VIM中的自定义命令组合map

- **map命令格式**(:map {lhs} {rhs})，几种前缀的微调效果：

1. nore（非递归）：递归(:map a b; :map c a; c就映射成了b)
2. n（normal）：普通模式下生效
3. v（visual）：可视模式下生效
4. i（insert）：插入模式下生效
5. c（command line）：命令行模式下生效

```vim
在作用模式下，输入td 等价输入:tabnew . <cr>,打开当前目录
:map td :tabnew .<cr> 
```
- 键表

```
<k0> - <k9>   小键盘 0 到 9
<S-...>  Shift＋键
<C-...>  Control＋键
<M-...>  Alt＋键 或 meta＋键
<A-...>  同 <M-...>
<Esc>  Escape 键
<Up>  光标上移键
<Space>  插入空格
<Tab>  插入Tab
<CR>  等于<Enter>

举例：
:inoremap <C-l> :set list <CR>:set listchars=tab:\\|\ <ESC>
按下ctrl＋l，将当前文件中的tab变成竖线
```

#### vimrc 自定义设置(当前用户的vim编辑器~/.vimrc)

```vim
"""""""""""""""""vim editor self definition"""""""""""""""""

set tabstop=4	"set tab as 4 space
set showcmd
set ai	"automatically indent
set shiftwidth=4	"the width of the auto shift
set autowrite	"auto save the file
set ruler	"show the cursor position at right bottom
syntax on	"highlight syntax,linux environment: set syntax=on
set completeopt=preview,menu "code auto complete
set clipboard+=unnamed "share the cut/paste board
set nu
set cursorline "show the current cursor line
"set list "显示特殊符号
"set listchars=tab:\|\ 	"显示tab符，并以｜高亮显示

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""############ AUTO Symbol Completion #########################
inoremap ( ()<ESC>i

inoremap [ []<ESC>i

inoremap { {<CR>}<ESC>O
 
inoremap " ""<ESC>i
inoremap ' ''<ESC>i
inoremap ` ``<ESC>i

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"auto Filetype c,cpp,py,rb set shiftwidth=4| set expandtab



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'"""""""""""
"""############ set file title ######################

filetype on
autocmd BufNewFile *.py,*.sh,*.rb exec ":call SetFiletitle()"

func SetFiletitle()
	call setline(1,"\#####################################################")
	call append(line("."), "\#	File Name: ".expand("%"))
	call append(line(".")+1, "\#	Author: Rachel Liu")
	call append(line(".")+2, "\#	Created Time: ".strftime("%Y-%m-%d"))
	call append(line(".")+3, "\#	Description: ")
	call append(line(".")+4, "\#	")
    call append(line(".")+5, "\#	Modified History: ")
	call append(line(".")+6, "\#	")		
	call append(line(".")+7, "\#	Copyright (C)".strftime("%Y")." All Rights Reserved")
	call append(line(".")+8, "\#####################################################")

	if expand("%:e") == 'sh' 
    	call append(line(".")+9, "\#!/usr/bin/bash")
	elseif expand("%:e") == 'py'
		call append(line(".")+9, "\#!/usr/bin/env python")
		call append(line(".")+10, "\#-*- coding:utf-8 -*-")
    endif
	set list
	set listchars=tab:\|\ 	
    autocmd BufNewFile * normal G
	
endfunc

```

---

To be Continued ...
