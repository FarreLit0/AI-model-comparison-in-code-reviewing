
package com.baeldung.application.entity;

import java.util.Date;

public class Customer {
    private String customerName;
    private Date joiningDate;

    public Customer(String customerName) {
        this.customerName = customerName;
        this.joiningDate = new Date();
    }

    public String getCustomerName() { 
        return this.customerName; 
    }

    public Date getJoiningDate() {
        return this.joiningDate;
    }
}
