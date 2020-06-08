
/*
 * Copyright (C) Igor Sysoev
 * Copyright (C) Nginx, Inc.
 */


#ifndef _NGINX_H_INCLUDED_
#define _NGINX_H_INCLUDED_


<<<<<<< HEAD
#define nginx_version      1017008
#define NGINX_VERSION      "1.17.8"
=======
#define nginx_version      1019001
#define NGINX_VERSION      "1.19.1"
>>>>>>> 2d4f04bba0613292d8b51bf0de959e88afc72c54
#define NGINX_VER          "nginx/" NGINX_VERSION

#ifdef NGX_BUILD
#define NGINX_VER_BUILD    NGINX_VER " (" NGX_BUILD ")"
#else
#define NGINX_VER_BUILD    NGINX_VER
#endif

#define NGINX_VAR          "%WLC_NGX_VAR%"
#define NGX_OLDPID_EXT     ".oldbin"


#endif /* _NGINX_H_INCLUDED_ */
