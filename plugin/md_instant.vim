
if !has('python3')
    echo "Error: Required vim compiled with +python3"
    finish
endif
com! -nargs=* Instantmd call OpenMarkdown()

let s:scriptfolder = expand('<sfile>:p:h').'/md_instant'

function! OpenMarkdown()
    let b:md_tick = 0
python3 << EOF
import sys, os, vim, time
sys.path.append(vim.eval('s:scriptfolder'))
sys.stdout = open(os.path.devnull, 'w')
sys.stderr = open(os.path.devnull, 'w')
vim.command(':autocmd!')
vim.command('autocmd InsertLeave * call UpdateMarkdown()')
vim.command('autocmd CursorMovedI * call UpdateMarkdown()')
vim.command('autocmd CursorMoved * call UpdateMarkdown()')
vim.command('autocmd VimLeavePre * call CloseMarkdown()')
import md_instant
md_instant.main()
md_instant.startbrowser()
#vim.command("let einfo = '%s'" % 's')
md_instant.sendall(vim.current.buffer)
EOF
endfunction

function! UpdateMarkdown()
    if (b:md_tick != b:changedtick)
        let b:md_tick = b:changedtick
python3 << EOF
md_instant.sendall(vim.current.buffer)
EOF
    endif
endfunction
function! CloseMarkdown()
python3 << EOF
md_instant.stopserver()
EOF
endfunction
