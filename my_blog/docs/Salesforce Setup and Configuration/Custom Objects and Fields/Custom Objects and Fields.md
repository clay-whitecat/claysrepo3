# Custom Objects and Fields Documentation

Custom objects and fields are used to extend the functionality of Salesforce. Custom objects are used to store data that is specific to an organization, and custom fields are used to capture additional information about the data. This document provides an overview of custom objects and fields, and describes best practices for creating and managing them.

## Custom Objects

Custom objects are used to store data that is specific to an organization. They are similar to standard objects, but they are created by the organization to meet specific business requirements. Custom objects can be used to store a wide range of data, such as customer information, product details, and order history. They can also be used to capture information about business processes, such as sales leads, support cases, and service requests.

### Custom Object Types

There are several types of objects that are commonly used in Salesforce. The following are the most common types of objects:
**Custom Objects**: Custom objects are used to store data that is specific to an organization. They are created by the organization to meet specific business requirements, and can be used to store a wide range of data, such as customer information, product details, and order history.
**Standard Objects**: Standard objects are provided by Salesforce, and are used to store common types of data, such as accounts, contacts, and opportunities. They are included in every Salesforce organization, and can be customized to meet specific business requirements.
**External Objects**: External objects are used to access data that is stored outside of Salesforce, such as in an external database or web service. They are defined in Salesforce, but the data is stored and managed in an external system.
**Big Objects**: Big objects are used to store large volumes of data that are accessed infrequently. They are optimized for data storage and query performance, and can be used to store data that is not suitable for standard or custom objects.

## Documenting Business Logic in Fields

A data dictionary is a document that describes the data that is stored in a database. It includes information about the tables, columns, and relationships that are used to store and retrieve data. A data dictionary is important because it helps to ensure that the data is accurate, consistent, and easy to use. It also helps to ensure that the data is well-documented, and that changes to the data are managed effectively. The following are the key components of a data dictionary:

To create a comprehensive overview of each object, we will have a per object template that details all describe info, and any additional information that is relevant to the object.

## Custom Object Template

| Field       | Description                            | Type     | Required | Unique | Default Value |
| ----------- | -------------------------------------- | -------- | -------- | ------ | ------------- |
| Field Name  | The name of the field                  | Text     | Yes      | No     | None          |
| Description | A description of the field             | Text     | No       | No     | None          |
| Type        | The data type of the field             | Text     | Yes      | No     | None          |
| Required    | Whether the field is required          | Checkbox | No       | No     | False         |
| Unique      | Whether the field value must be unique | Checkbox | No       | No     | False         |
