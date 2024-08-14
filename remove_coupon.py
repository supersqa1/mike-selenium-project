
from selenium import webdriver
from selenium.webdriver.common.by import By


product_page_url = "http://dev.bootcamp.store.supersqa.com/product/album/"

#create the browser

driver = webdriver.Chrome()
driver.implicitly_wait(10)

#go to the product page

driver.get(product_page_url)

#click on add to cart

add_to_cart_locator = '//*[@id="product-24"]/div[2]/form/button'
add_to_cart_btn = driver.find_element(By.XPATH, add_to_cart_locator)

#Click on the add to cart button

add_to_cart_btn.click()

#Go to cart

view_cart_locator = '//*[@id="content"]/div/div[1]/div/a'
view_cart_btn = driver.find_element(By.XPATH, view_cart_locator)
view_cart_btn.click()

#input coupon code

coupon_code = 'ssqa100'
coupon_code_field = driver.find_element(By.ID, 'coupon_code')
coupon_code_field.send_keys(coupon_code)

#Apply coupon

apply_coupon_btn_locator = '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/div/button'
apply_coupon_btn = driver.find_element(By.XPATH, apply_coupon_btn_locator)
apply_coupon_btn.click()


#remove coupon

coupon_remove_btn_locator = '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[2]/td/a'
coupon_remove_btn = driver.find_element(By. XPATH, coupon_remove_btn_locator)
coupon_remove_btn.click()

#Verify success message

success_message_locator = '//*[@id="post-7"]/div/div/div[1]/div'
success_message = driver.find_element(By.XPATH, success_message_locator)
displayed_message = success_message.text
expected_message = "Coupon code applied successfully."
if displayed_message != expected_message:
    raise Exception(f"After removing the coupon the expected message do not match with the expected message")
else:
    print("PASS")


breakpoint()


