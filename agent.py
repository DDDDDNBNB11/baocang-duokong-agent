import argparse
from web import run_server

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='合约爆仓多空观测智能体')
    sub = p.add_subparsers(dest='command', required=True)
    w = sub.add_parser('web')
    w.add_argument('--port', type=int, default=8001)
    args = p.parse_args()
    run_server(args.port)
