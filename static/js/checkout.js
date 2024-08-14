const form=document.getElementById("form")
const total = '{{order.get_cart_total}}'; 
const shipping='{{order.shipping}}'

if (shipping == 'False'){
    document.getElementById('shipping-info').innerHTML=''
}

form.addEventListener('submit',function(e)
{
    e.preventDefault()
    console.log("Form gönderildi..")
    document.getElementById('form-button').classList.add('hidden')
    document.getElementById('payment-info').classList.remove('hidden')
})

document.getElementById('make-payment').addEventListener('click',function(e){
    submitFormData()
})


function submitFormData(){
    console.log("Ödeme buttonuna tıkladın....")
   
    const userFormData={
        'name':null,
        'email':null,
        'total':total,
    }

    const shippingInfo={
        'address':null,
        'city':null,
        'state':null,
        'street':null,
    }

    if(shipping != 'False')
    {
        shippingInfo.address=form.address.value
        shippingInfo.city=form.city.value
        shippingInfo.state=form.state.value
        shippingInfo.street=form.street.value
    }

    if(user == 'AnonymousUser'){
        userFormData.name=form.name.value
        userFormData.email=form.email.value
    }

    const url='/process_order/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'form': userFormData,
            'shipping': shippingInfo,
        })
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('success', data);
        alert('İşlem tamamlandı..');
        window.location.href = "{% url 'coffee' %}";
    })

}



