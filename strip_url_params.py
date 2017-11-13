def strip_url_params(url, params_to_strip = []):
    main, *params = url.replace('?', '&').split('&')
    param_dict = {}
    for param in params:
        key, value = param.split('=')
        if key not in params_to_strip and key not in param_dict.keys():
            param_dict[key]= value

    return main + '?' + '&'.join(key+'='+value for key,value in sorted(param_dict.items())) if param_dict else main
    
    
url = 'www.codewars.com'