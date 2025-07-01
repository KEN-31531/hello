//+------------------------------------------------------------------+
//|                        TurtleBreakout.mq4                        |
//|   Simple Turtle Breakout example Expert Advisor for MetaTrader 4 |
//|   This code is for educational purposes only.                    |
//+------------------------------------------------------------------+
#property strict

extern int    BreakoutPeriod = 20;   // lookback period for breakout
extern int    StopPeriod     = 10;   // period for stop exit
extern double Lots           = 0.1;  // lot size
extern int    Slippage       = 3;    // allowed slippage

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
   // Check if there are open positions on current symbol
   if(OrdersTotal() > 0)
      return;

   double highest = iHigh(NULL,0,iHighest(NULL,0,MODE_HIGH,BreakoutPeriod,1));
   double lowest  = iLow(NULL,0,iLowest(NULL,0,MODE_LOW,BreakoutPeriod,1));
   double stopHigh= iHigh(NULL,0,iHighest(NULL,0,MODE_HIGH,StopPeriod,1));
   double stopLow = iLow(NULL,0,iLowest(NULL,0,MODE_LOW,StopPeriod,1));

   // Buy breakout
   if(Close[1] > highest)
     {
      double sl = stopLow;
      OrderSend(Symbol(),OP_BUY,Lots,Ask,Slippage,sl,0,"TurtleBreakout BUY",0,0,Blue);
     }
   // Sell breakout
   else if(Close[1] < lowest)
     {
      double sl = stopHigh;
      OrderSend(Symbol(),OP_SELL,Lots,Bid,Slippage,sl,0,"TurtleBreakout SELL",0,0,Red);
     }
  }

//+------------------------------------------------------------------+

