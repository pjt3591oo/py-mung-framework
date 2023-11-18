import time

def route_resolve_print(method, path):
  print('\033[32m [{project_name}] \033[33m {level} \033[37m {dt} \033[33m [{type}] \033[32m Mapped {path} {method} \033[0m'.format(project_name='mung_test', dt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), level='info', type='RouterExplorer', path='{ ' + path + ' }', method=method))
  

def application_start_print():
  print('\033[32m [{project_name}] \033[33m {level} \033[37m {dt} \033[33m [{type}] \033[32m Starting Mung Application... \033[0m'.format(project_name='mung_test', dt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), level='info', type='MungFactory'))

