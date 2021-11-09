<h1>solrorm : A sort-of solr ORM for python</h1>

<ul>
<li>solrpy - deprecated</li>
<li>solrorm - currently in dev</li>
</ul>

<h2>Usage</h2>

<h3><u>Cores</u></h3>
The first step to interact with solr using solrorm is to define a core.
Core objects can be initialized using the solrorm.cores.Core class. 

<u>Example</u>
<code>
<br>from solrorm.cores import Core
<br>my_core = Core(host='xxx.xx.x.xxx', port = 8983, core_name = 'core_name_here', fields = ['title', 'authors'])

</code>

<h3><u>Queries</u></h3>
queries helps us to filter records from solr. Using solrorm, we can pass arguments and various 'magic' arguments to filter records.
A few example are shown below.
<u>Example</u>
<code>
<br>results = my_core.objects.query(organizations="twitter inc", __tag ="it", sentiment="Positive").get(start=10, rows=1)

</code>
<br> Double underscore (__) after an argument name means that is is negated. In this case, it means source_tag != "it_news"
<br>' __in'  after an argument specifies range query. It can be used to filter for example, records in a certain range of dates.


<h3><u>Response</u></h3>
After a query is executed we will get a response object. The response object will have the following fields.
<br>1) docs : the docs returned from solr
<br>2) total : total counts matching in solr
<br>3) count : the size of a page (useful for pagination)

The response object also offers a handy transform method. Please refer the attached example file to find the usage.