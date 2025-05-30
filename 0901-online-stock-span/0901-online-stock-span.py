class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span_count = 1

        while self.stack and self.stack[-1][0] <= price:
            span_count += self.stack.pop()[1]
        self.stack.append((price, span_count))

        return span_count
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)