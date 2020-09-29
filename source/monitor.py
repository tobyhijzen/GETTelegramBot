#!/usr/bin/python3

# Telegram setup
token = '1366223946:AAEABFGgJOrSjrrZm4i0CAD5Y0O5BKqGLdQ'

import time
import struct
import datetime

from telegram import Bot
bot = Bot(token=token)

# UNIswap setup

from web3.auto.infura.mainnet import w3

NETWORK = "mainnet"

GET_WETH_PAIR_FACTORY_ADDRESS = {

"mainnet": "0x2680a95fc9de215f1034f073185cc1f2a28b4107",

}

GET_WETH_PAIR_FACTORY_ABI = """[
{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},
{
    "anonymous":false,
    "inputs":[
        {"indexed":true,"internalType":"address","name":"from","type":"address"},
        {"indexed":true,"internalType":"address","name":"to","type":"address"},
        {"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}
    ],
    "name":"Transfer","type":"event"},
{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
{
    "constant":false,
    "inputs":[
        {"internalType":"address","name":"from","type":"address"},
        {"internalType":"address","name":"to","type":"address"},
        {"internalType":"uint256","name":"value","type":"uint256"}
        ],
    "name":"transferFrom",
    "outputs":[{"internalType":"bool","name":"","type":"bool"}],
    "payable":false,"stateMutability":"nonpayable","type":"function"
}
]"""

# get_weth_checksum_address = w3.toChecksumAddress('0x2680a95fc9de215f1034f073185cc1f2a28b4107')
get_weth_checksum_address = w3.toChecksumAddress('0x8a854288a5976036a725879164ca3e91d30c6a1b')

GET_WETH_PAIR_CONTRACT = w3.eth.contract(address=get_weth_checksum_address, abi=GET_WETH_PAIR_FACTORY_ABI)

# block = "latest"
# block = 10955000
block = 10947084

myfilter = GET_WETH_PAIR_CONTRACT.events.Transfer.createFilter(fromBlock=block)

handled_blocks = []

connected = True

print('Monitoring transactions')

while True:
    # Try to connect tot infura node and get logs
    try:
        transactions = w3.eth.getFilterLogs(myfilter.filter_id)
    except:
        if connected:
            t = datetime.datetime.now()
            print("Internet connection timed out at: ", t) 
            connected = False
        time.sleep(10)
        continue
    
    # Succesfully connected!
    if not connected:
        t = datetime.datetime.now()
        print("Reconnected to server at ", t)
        connected = True

    # Handle all transactions
    new_handled_blocks = []
    for i in range(0,len(transactions)):
        block_number = transactions[i]['blockNumber']
        if not (block_number in handled_blocks):
            print('\nblock nr:',block_number)
            tx_hash = transactions[i]['transactionHash']
            print('Transaction hash: 0x' + ''.join('{:02x}'.format(x) for x in tx_hash))
            receipt = w3.eth.getTransactionReceipt(tx_hash)
            print('\n\n')
            print(receipt)
            print('\n\n')
            from_address = receipt['from']
            to_address = receipt['to']
            print('from: ', from_address)
            print('to:   ', to_address)
            print('\n\n')

            get_value = 0
            weth_value = 0
            for i in range(0,len(receipt.logs)):
                operation = ''.join('{:02x}'.format(x) for x in receipt.logs[i].topics[0])
                if receipt.logs[i].address == '0x8a854288a5976036A725879164Ca3e91d30c6A1B' and \
                    operation == 'ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef':
                    hexdata_string = receipt.logs[i].data[2:]
                    data = struct.unpack('!QQQQ',bytes.fromhex(hexdata_string))
                    get_value = data[3]*10.**-18 + data[2]*2**64*10**-18
                if receipt.logs[i].address == '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2' and \
                    operation == 'ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef':
                    hexdata_string = receipt.logs[i].data[2:]
                    data = struct.unpack('!QQQQ',bytes.fromhex(hexdata_string))
                    weth_value = data[3]*10.**-18 + data[2]*2**64*10**-18
                if weth_value != 0 and get_value != 0:
                    msg_text = 'Added liquidity: ' + str(get_value) + ' GET | ' + str(weth_value) + ' ETH'
                    bot.send_message(chat_id=-466074155, text=msg_text)
                    time.sleep(1)
                    break

            if not (block_number in new_handled_blocks):
                new_handled_blocks.append(block_number)
    handled_blocks += new_handled_blocks
    time.sleep(60)