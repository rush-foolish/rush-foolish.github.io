"""""""""""""""""vim editor self definition"""""""""""""""""

set tabstop=4	"set tab as 4 space
set showcmd
set ai	"automatically indent
set shiftwidth=4	"the width of the auto shift
set autowrite	"auto save the file
set ruler	"open status bar ruler
set syntax=on	"highlight syntax

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""############ AUTO Symbol Completion #########################
inoremap ( ()<ESC>i

inoremap [ []<ESC>i

inoremap { {<CR>}<ESC>O
 
inoremap " ""<ESC>i
inoremap ' ''<ESC>i


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"auto Filetype c,cpp,py,rb set shiftwidth=4| set expandtab



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'"""""""""""
"""############ set file title ######################
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

    autocmd BufNewFile * normal G

endfunc
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

filetype on
