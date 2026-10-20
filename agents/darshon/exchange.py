# The exchange: an order book for one product, like one item in the Bazaar.
# Agents post orders here; later, their tools will call these functions.
import heapq as hq
# Every order that is waiting to be filled lives in one of these two lists.
buy_orders = []   # people who want to buy
sell_orders = []  # people who want to sell
ORDER_NUM = 0

def place_order(agent, side, price, amount):
    """Add an order to the book. side is "buy" or "sell"."""
    # TODO(human)

    if side == "buy":
        if price > sell_orders:
            hq.heappush(buy_orders, (price, agent, ORDER_NUM))


        ORDER_NUM += 1


# Try it out
place_order("Alice", "buy", 10, 5)   # Alice wants 5 items, will pay 10 each
place_order("Bob", "sell", 12, 3)    # Bob has 3 items, wants 12 each
print("buy orders:", buy_orders)
print("sell orders:", sell_orders)
