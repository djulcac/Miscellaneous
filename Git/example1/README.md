# 01 Push to different servers

Configurar el archivo ./git/config, inicialmente se puede ver:
```
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[remote "origin"]
        url = https://github.com/djulcac/Miscellaneous.git
        fetch = +refs/heads/*:refs/remotes/origin/*       
[branch "master"]
        remote = origin
        merge = refs/heads/master
[user]
        email = djulcac@uni.pe
        name = Danny JC
```

Si queremos agrear un segundo servidor, por ejemplo gitlab, se edita
la seccion de [remote "origin"]
```
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[remote "origin"]
        url = https://github.com/djulcac/Miscellaneous.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[remote "gitlab"]
        url = https://gitlab.com/djulcac/Miscellaneous.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
[user]
        email = djulcac@uni.pe
        name = Danny JC
```