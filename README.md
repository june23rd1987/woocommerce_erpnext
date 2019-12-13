## Woocommerce Erpnext https://ovresko.com/
based on https://github.com/ashish-greycube/woocommerce_erpnext

2Way Integration between WooCommerce and ERPNext

Items, Order, Order Status, Stock level, 
changes:
- Update order status after delivery note submit=> completed or cancel=> cancelled
- update item image once 
- actual stock quantity updated on daily schedule
- added fields (sku, handle stock, Stock Qty based on warehouse in woo settings, favorite)

# Install:

- Install with bench get-app / bench install-app
- Add Custom fields in Woocommerce Settings : 
	-Price List / Link / price_list
	-Price List / Link / promo_price_list (for promo prices)
	
Order Sync replace the used in  https://github.com/frappe/erpnext/blob/develop/erpnext/erpnext_integrations/connectors/woocommerce_connection.py
with content of file new_connector.py

- To put sync (custom) button in "Woocommerce Settings", to sync all items.
- On Save of Individual Item, sync Item from ERPNext to Woocommerce ( through the code attached below )
- While saving individual item in ERPNext, check if the item exist in woocommerce, if yes update else create new 
- To check if the direct web link for the item images from erpnext 

### add custom script for Woocommerce Settings doctype. can be exported as fixture

```
frappe.ui.form.on('Woocommerce Settings', {
	refresh(frm) {
    frm.add_custom_button(__("Sync Items to WooCommerce"), () => {
      frappe.call({
        method: "woocommerce_erpnext.woo_connector.sync_all_items"
      });
    });
	}
})
```

#### License

MIT
