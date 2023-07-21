from utils import drivers


def before_all(context):
    drivers.launch_browser(context)


def before_feature(context, feature):
    print(f'-----Feature: {feature}-----')


def before_scenario(context, scenario):
    print(f'Started execution of {scenario.name}')
    context.driver.get(context.config.userdata['base_url'])


def after_all(context):
    drivers.terminate_browser(context)
