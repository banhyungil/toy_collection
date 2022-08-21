$(document).ready(function () {
  selectBucket();
});

function selectBucket() {
  $.ajax({
    type: "GET",
    url: "/bucket/selectBucket",
    data: {},
    success: function (res) {
      $("#bucket-list").empty();
      bucketList = res['bucket_list'];

      for (const oBucket of bucketList) {
        console.log(oBucket);
        const bucketHtml = createBucketHtml(oBucket.bucket, oBucket.isDone, oBucket._id);
        $("#bucket-list").append(bucketHtml);
      }
    }
  });

  function createBucketHtml(bucket, isDone, docId) {
    let buttonElt = '';
    let h2Elt = '';
    

    if(!isDone) {
      h2Elt = `<h2>✅ ${bucket}</h2>`;
      buttonElt = `<button onclick="saveBucketDone(this)" data-id="${docId.$oid}" type="button" class="btn btn-outline-primary">완료!</button>`

    }else {
      h2Elt = `<h2 class="done">✅ ${bucket}</h2>`

    }

    return `<li>
              ${h2Elt}
              ${buttonElt}
            </li>`
  }
}
function saveBucket(){
  const bucket = $('#bucket').val();

  $.ajax({
    type: "POST",
    url: "/bucket/saveBucket",
    data: {bucket: bucket},
    success: function (res) {
      selectBucket();
    }
  });
}

function saveBucketDone(target){
  console.log(target);
  const objectId = target.dataset.id;
  console.log(objectId);

  $.ajax({
    type: "POST",
    url: "/bucket/saveBucket/done",
    data: {'objectId': objectId},
    success: function (res) {
      selectBucket();
    }
  });
}