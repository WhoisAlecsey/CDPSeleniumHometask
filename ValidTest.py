from HelperFunctions import WebElementActions
from HelperFunctions.Constants import Constants


def test1_GoogleCloudPlatformPricingCalculator():
    action = WebElementActions.Actions()

    action.open_the_web_site("http://cloud.google.com/")
    action.click_on_element(Constants.search_box)
    action.write_the_message_in_the_field(Constants.search_box, 'Google Cloud Platform Pricing Calculator')
    action.click_on_element(Constants.see_all_results)
    action.the_element_is_displayed(Constants.google_cloud_calculator_link)
    action.click_on_element(Constants.google_cloud_calculator_link)
    action.change_the_frame("myFrame")
    action.click_on_element(Constants.compute_engine_tab)
    action.write_the_message_in_the_field(Constants.number_of_instances, '4')
    action.select_dropdown_value(Constants.operating_system, Constants.operating_system_value_free)
    action.select_dropdown_value(Constants.machine_class, Constants.machine_class_value_regular)
    action.select_dropdown_value(Constants.machine_type, Constants.machine_type_value_n1_standard_8)
    action.set_the_checkbox(Constants.add_gpus)
    action.select_dropdown_value(Constants.number_of_gpus, Constants.number_of_gpus_value_1)
    action.select_dropdown_value(Constants.gpu_type, Constants.gpu_type_value_tesla_v100)
    action.select_dropdown_value(Constants.local_ssd, Constants.local_ssd_value_2x375)
    action.select_dropdown_value(Constants.datacenter_location, Constants.datacenter_location_value_frankfurt)
    action.select_dropdown_value(Constants.commited_usage, Constants.commited_usage_value_1_year)
    action.click_on_element(Constants.add_to_estimate)

    action.assert_element(Constants.estimate_vm_class, "VM class: regular")
    action.assert_element(Constants.estimate_instance_type, "Instance type: n1-standard-8")
    action.assert_element(Constants.estimate_region, "Region: Frankfurt")
    action.assert_element(Constants.estimate_available_ssd, "Total available local SSD space 2x375 GB")
    action.assert_element(Constants.estimate_commitment_term, "Commitment term: 1 Year")

    action.close_browser()
