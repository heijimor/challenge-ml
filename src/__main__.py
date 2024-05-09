# init
from app.app import run_server

if __name__ == '__main__':
  try: 
    run_server()
  except:
    print('error')