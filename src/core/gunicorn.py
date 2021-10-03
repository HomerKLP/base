from multiprocessing import cpu_count

bind = "0.0.0.0:8000"
worker_class = "gthread"
workers = cpu_count() * 2 + 1
threads = 4
max_requests = 4096
max_requests_jitter = 256
capture_output = True
preload_app = True
