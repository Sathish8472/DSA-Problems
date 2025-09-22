class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track the maximum profit for up to two transactions.
        # buy1: max profit after the first buy.
        # sell1: max profit after the first sell.
        # buy2: max profit after the second buy.
        # sell2: max profit after the second sell.
        # We initialize buys to a very small number and sells to 0.
        self.initialize_transaction_states()

        # Iterate through each price in the prices list.
        for price in prices:
            # For each price, update the four state variables.
            self.update_transaction_states(price)

        # The final result is the maximum profit achievable after the second sell,
        # which encompasses the profit from 0, 1, or 2 transactions.
        return self.get_final_profit()

    def initialize_transaction_states(self):
        # Set initial profit after the first buy.
        self.buy1 = -float('inf')
        # Set initial profit after the first sell.
        self.sell1 = 0
        # Set initial profit after the second buy.
        self.buy2 = -float('inf')
        # Set initial profit after the second sell.
        self.sell2 = 0

    def update_transaction_states(self, price: int):
        # Update the maximum profit after the first buy:
        # max(current_buy1, profit_from_buying_now)
        # The profit from buying now is -price since we start with 0 capital.
        self.buy1 = max(self.buy1, -price)
        
        # Update the maximum profit after the first sell:
        # max(current_sell1, profit_from_selling_now)
        # The profit from selling is the profit from the first buy state plus the current price.
        self.sell1 = max(self.sell1, self.buy1 + price)

        # Update the maximum profit after the second buy:
        # max(current_buy2, profit_from_buying_again)
        # Profit from buying again is the profit from the first sell state minus the current price.
        self.buy2 = max(self.buy2, self.sell1 - price)

        # Update the maximum profit after the second sell:
        # max(current_sell2, profit_from_selling_again)
        # Profit from selling again is the profit from the second buy state plus the current price.
        self.sell2 = max(self.sell2, self.buy2 + price)

    def get_final_profit(self) -> int:
        # Return the final calculated profit for the second sell.
        return self.sell2