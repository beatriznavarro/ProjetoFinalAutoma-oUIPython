from pages.AddCustomerPage import AddCustomerPage
from pages.CustomersPage import CustomersPage
from pages.ManagerPage import ManagerPage


class TestFilterCustomer:

    def test_filter_customer(self, setup):
        menu_page = setup
        menu_page.open_bank_manager_login()
        manager_page = ManagerPage(driver=menu_page.driver)
        # valida que está na pagína de gerenciamento de cliente
        assert manager_page.is_url_manager_page(), 'Página de gerenciamento não encontrada!'


        # Add cliente
        manager_page.click_add_customer()
        add_customer = AddCustomerPage(driver=manager_page.driver)
        add_customer.fill_first_name('Maria')
        add_customer.fill_last_name('Silva')
        add_customer.fill_post_code('13174-100')
        add_customer.click_add_customer()
        add_customer.check_message_success()

        # Listagem do cliente
        manager_page.click_customers()
        # Valida que está na página de listar clientes
        customers_page = CustomersPage(driver=add_customer.driver)

        assert customers_page.is_url_customer_page(), 'Página de listar clientes não encontrada!'

        # Busca Cliente
        customers_page.find_customer('Maria')

        # Valida busca do cliente
        assert customers_page.check_table() == 1, 'Cliente não encontrado'
