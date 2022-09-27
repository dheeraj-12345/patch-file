From 7f02102ccb465bc13fae70218065d3faabeb8fae Mon Sep 17 00:00:00 2001
From: Mahankali dheeraj <dheeraj0169@gmail.com>
Date: Tue, 27 sep 2022 10:08:13 +0530
Subject: [PATCH] Create patch file

---
 client3.py     | 12 ++++++++----
 client_test.py |  7 +++++--
 2 files changed, 13 insertions(+), 6 deletions(-)

diff --git a/client3.py b/client3.py
index f1771c3..220a692 100644
--- a/client3.py
+++ b/client3.py
@@ -35,25 +35,29 @@ def getDataPoint(quote):
 	stock = quote['stock']
 	bid_price = float(quote['top_bid']['price'])
 	ask_price = float(quote['top_ask']['price'])
-	price = bid_price
+	price = (bid_price + ask_price)/2
 	return stock, bid_price, ask_price, price
 
 def getRatio(price_a, price_b):
 	""" Get ratio of price_a and price_b """
 	""" ------------- Update this function ------------- """
 	""" Also create some unit tests for this function in client_test.py """
-	return 1
+	if(price_b==0):
+		return
+	return price_a/price_b
 
