# Snowflake Course 12/06/2025

## Snowflake overview:
- Easy to use
- Auto administration. No manual tuning
- Auto performance improvements
- Instant scalability. Scales up and down with no downtime
- Unified cost management. Visibility and optimistation of costs
- Integrated ML and AI LLM tools and ops monitoring 

User **HIPPO01**

**Training works for 30days**
https://app.snowflake.com/sfedu05/ohb42832/#/notebooks

---

## What is a Warehouse in Snowflake? 📓

### Defining "Warehouse" in Snowflake:

People who have been working with data for a while might think of the term "Data Warehouse" as referring to a special collection of data structures, but in Snowflake, warehouses don't store data.

In Snowflake, warehouses are "compute resources" - they are used to perform the processing of data.

When you create a warehouse in Snowflake, you are defining these "resources".

**Scaling Up and Down:**

Changing the size of warehouse changes the number of servers in the cluster.

Changing the size of an existing warehouse is called scaling up or scaling down.

**Scaling In and Out:**

If multi-cluster/elastic warehousing is available (Enterprise edition or above), a warehouse is capable of scaling out in times of increased demand.

If multi-cluster scaling out takes place, clusters are added for the period of demand, and then clusters are removed (snap back) when demand decreases.

The number of servers in the original cluster dictates the number of servers in each cluster during periods where the warehouse scales out by adding clusters.

---

## Just Because You Can...📓

### ...Doesn't Mean You SHOULD!!! 📓

In Snowflake, you can bring ENORMOUS compute power into play in just a few seconds! We want you to know this is possible, especially if you have a large job that needs LARGE computing power.

But, we also want you to know that most queries DO NOT require massive computing power.

In fact, Snowflake recommends always starting with extra-small (XS) warehouses and only scaling up if you find a compelling reason to do that. XS warehouses use one credit per hour. Our largest warehouse is the Snowpark-optimized 6XL, which uses a whopping 768 credits per hour! More than 38 credits per minute!

For this workshop, keep your warehouse set to XS except in cases where we ask you to use size S instead.

For on-the-job Snowflake usage, you will likely have people who oversee the configuration of your warehouses. Warehouse oversizing is the simplest way to make mistakes that cause big surprises on the monthly invoice, so it's best to get accustomed to using XS and S warehouses most of the time and scale up only after careful consideration.

Snowflake recommends that each account have people who oversee costs and will have advanced knowledge of how to choose warehouse sizes best and configure the elasticity settings. These cost administrators will also be able to calculate whether the change in warehouse-size will result in enough time savings to justify the costs incurred or even balance them out.

---

