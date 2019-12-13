## Woocommerce Erpnext

Integration between WooCommerce and ERPNext

# Install:

    # from frappe-bench folder
    # source ./env/bin/activate
    # pip install woocommerce
    # deactivate
    # Setup:

- Copy the existing woo-commerce connector "order" function in custom app
  https://github.com/frappe/erpnext/blob/develop/erpnext/erpnext_integrations/connectors/woocommerce_connection.py#L23

- Edit the code in point 1 to Ignore Item Edit / Creation , it should just link existing items in Sales Order.

- To put sync (custom) button in "Woocommerce Settings", to sync all items.

- On Save of Individual Item, sync Item from ERPNext to Woocommerce ( through the code attached below )

- While saving individual item in ERPNext, check if the item exist in woocommerce, if yes update else create new ( At present in point 4 , it creates new items in woocommerce)

- To check if the direct web link for the item images from erpnext ( e.g. http://demo.erpnext.com/files/two_apple-copiar.jpg(170 kB)
  http://demo.erpnext.com/files/two_apple-copiar.jpg
  ) can be linked to items in woocommerce

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
