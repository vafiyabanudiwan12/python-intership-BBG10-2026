newsletter_subscribers ={ "alice@email.com", "bob@email.com", "chaelie@eamil.com",}

purchasers ={"bob@email.com", "chaelie@email.com", "david@email.com"}
subscribers_no_purchase = newsletter_subscribers - purchasers

purchasers_not_subscribed = purchasers - newsletter_subscribers

print("subscribers without purchase:", subscribers_no_purchase)
print("purchasers who never subscribed:", purchasers_not_subscribed)
