#!/bin/bash

echo "Running ShippingApp for multiple orders..."
echo

for order_id in 1001 1002 1003
do
echo "============================"
echo "Running order ID: $order_id"
echo "============================"

python3 -m legacy_code.src.ShippingApp "$order_id"

echo
done

echo "Done."

read -p "Press Enter to continue..."