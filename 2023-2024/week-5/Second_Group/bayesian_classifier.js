var values;

const input = document.getElementById('input')
input.addEventListener('change', () => {
  readXlsxFile(input.files[0]).then((rows) => {
    // reads the xsl file
    // The then method is used to handle the asynchronous result of reading the file.
    //لێرە ریزێک دەگەرێنێتەوە کە هەر ریزێک بریتتیە لە خانەکان
    // واتا یەک ئەرەی گەورە کە هەموو زانیاریەکانی تێدایە

    let inputs = rows;
    // ئەم ڤاریەبڵە هیچ ناکات
    values = calculatedTable(inputs);
    // زانیاریەکان ئەکەینە ناو ئەم ڤاریەبڵە تاکو بتوانین دوایی لە کاتی حەلکردنی زانیاری نوێ بەکاریان بهێنین لە خوارەوەیە
  })
})


function calculatedTable(rows){
    console.log(rows)


    // Calculate each one separately
    let labels = rows[rows.length-1];
    console.log("Labels", labels);
    //لێرە تەنها ناوی لەیبڵەکانمان وەرگرتووە، واتا جیامانکردوەتەوە لە ئەرەییە گشتیەکە
    // 2D array(but here we use objects) containing both label and value of it

    //specify the size of the labels
    let prob = Array.from({ length: rows[rows.length - 1].length - 1 }, () => ({}));
    console.log(prob )
    // لێرە ئەررەیەکمان دروست کردووە کە ئۆبچێتی تێدایە بەپێی ژمارەی لەیبڵەکان ئۆبچێکتی تێدەکەین تاکو حساباتی هەریەکە لە لەیبڵەکانیان لە ناو بکەین

    for(let row =0; row< rows.length-2; row++){
        
        for(let column =0; column< rows[row].length-1; column++){
            
            prob[column][rows[row][column]+","+rows[row][rows[row].length-1]] = 0;
            // لێرە یەکەمجار نرخی هەموویان دەکەین بە سفر، بەڵام نرخی لەیبڵەکان پێکەوە دەنوسین لەگەڵ ئەوەی کە دەمانەوێت بیدۆزینەوە
            // بەم جۆرە
            // like this: N,Mild
        }
    } 

    // Get key's separate them and check whether it should be added or not.
    // console.log(Object.keys(prob[0]))
    for(let row =0; row< rows.length-1; row++){
        
        for(let column =0; column< rows[row].length-1; column++){
            
            prob[column][rows[row][column]+","+rows[row][rows[row].length-1]] += 1;
            // لێرە هەرکاتێک کە یەکێکی وەکو خۆی هەبوو پێیدەڵێین کۆ یەکی بکات، واتای چەند لەوەمان هەیە
            // لە جاڤاسکریپت ئۆبجێکتەکان گەر کێی هەبوو دوبارە ناینوسێت هەر کار لەسەر خۆی دەکات
        }
    } 

    //Now get the ration of their errors.
    //Devide each one of them by the last label y or n(here).

    // first get the last label result:
    let required_label = {}
    //ئەم ئۆبجێکتەش تەنها تایبەتە بەوەی کە دەمانەوێت بیدۆزینەوە، خۆمان هەندێک نرخمان پێیداوە تاکو لەیبڵی کۆتایی بدۆزینەوە
    for(let row =0; row< rows.length-2; row++){
        
        required_label[ rows[row][rows[row].length-1 ] ] = 0;
        // نرخەکەی هەمووی دەکەین بە سفر
    } 

    // Get the repeated words
    for(let row =0; row< rows.length-1; row++){
        
        required_label[ rows[row][rows[row].length-1 ] ] += 1;
        // لێرە بزانین چەند دووبارە هەیە
    } 
    console.log( required_label, 'required label' )


    // second calculate each of them depending on that
    for(let row=0; row<prob.length; row++){

        const keys = Object.keys(prob[row]);
        for(let key of keys){
            const array_of_categories = key.split(",");
             prob[row][key] = prob[row][key] / required_label[array_of_categories[1]];
            //  لێرە حساباتی نرخەکان دەکات بۆ هەر یەک لا نرخی لەیبڵەکان
        }   

    }

    // Calculated probabilities
    
    // Now display the probabilities to the html file

    const required_label_length = Object.keys(required_label).length;
    // تانها کێیەکان دەهێنێتەوە چوونکە ئەمانەوێت نرخی وەربگرین

    let required_label_values = Array.from({ length: required_label_length }, () => ([]));
    // لێرە ئەوە زیادەیە کارمان پێی نەکردووە  

    const calculated_table = document.getElementById('calculated-table')
    // ئەمانەوێت زانیاریە حسابکراوەکان بکەینە ناو ئەم خشتەیە

    const keys_required_labels = Object.keys(required_label)
    // لێرە تەنها کێیەکانمان وەرگرتووە بۆ لەیبڵە داواکراوەکە

    const copy_required_label2 = { ...required_label };
    // ، بەمجۆرە کۆپی دەکەین تاکو رێفرێنسەکەی وەرنەگرێت و نرخەکان لە هەردوو شوێن دەستکاری نەکرێن کاتێک لە یەکیان دەستکاریمانکرد ئەمانتوانی بەکاریشی نەهێنین

    const sum_of_required_label = Object.values(required_label).reduce((acc, value) => acc + value, 0);
    // لێرە کۆی هەموو نرخی لەیبڵە داواکراوەکە دەکات

    for(let key of keys_required_labels){
        copy_required_label2[key]= copy_required_label2[key]/sum_of_required_label;
        // لێرە نرخی سەرەکی هەردوویکان بە رێژە(پۆینت) وەردەگرێت
    }

    console.log(copy_required_label2, ' is the copy required label')
    let html = "<table id='tobedownloaded'>";
    // لێرە تەنها دانانەوەیە ئەیخەینە ناو ڤاریەبڵێک پاشان لە سەر وێبەکە پیشانی ئەدەین

    html+= "<tr>";
    for(let key of keys_required_labels){
        html+= "<th>";
        html+= "P("+labels[labels.length-1]+"="+key+")="+copy_required_label2[key];
        html+= "</th>";
    }
    // ئەوەیان تەنها بۆ لەیبڵە داواکراوەکەیە
    html+= "</tr>";

    for (let row=0; row<prob.length; row++){

        html+= "<tr>";
        const keys = Object.keys(prob[row]);
        for(let key of keys){
            const array_of_categories = key.split(",");
            // ئێمە لەیبڵەکانمان لەسەرەوە بە فاریزە دانابوو لێرە جیایاندەکەینەوە تاکو بتوانین پیشانیان بدەینەوە
            html+= "<td>";
            html+= "p("+labels[row]+"="+array_of_categories[0]+","+labels[4]+"="+array_of_categories[1]+")="+ prob[row][key].toFixed(2);
            html+= "</td>";
        }

        html+= "</tr>";


    }
    // ئەوەشیان بۆ لەیبڵەکانی کەیە
    html+= "</table>";

    console.log(html)
    calculated_table.innerHTML = html;
    // لێرە دەیخەینە ناو تاگی دیاریکراو 






    // For the user entry
    calculateValue(rows, labels, prob, required_label);
    // لێرەش کار لەسەر ئەو نرخەدەکەین کە بەکارهێنەر زیادی کردووە

    return {
        rows,
        labels,
        prob,
        required_label
    };
    // ئەمانەش ئەخەینە ناو ڤاریەبڵی
    // values
}



function calculateValue(rows, labels, prob, required_label ){

    console.log(labels, prob, required_label);

    const label_html = document.getElementById("labels")
    // نرخی لەیبڵەکان لێرە دادەنێین تاکو بەکارهێنەر بتوانێت خۆی دیاریبکات
    let html="";
    for(let row = 0; row<labels.length-1; row++){
        html+= "<div>";
        html+= "<label for='"+labels[row]+"'>"+labels[row]+"</label>";
        // add select and its values with onclick if possible
        html+= "<select name='"+labels[row]+"' class='select-labels'>";

        const keys = Object.keys(prob[row]);

        const firstWords_in_keys = keys.map((element) => element.split(',')[0]);

        let removed_duplicate_keys = firstWords_in_keys.filter((value,index,self) => self.indexOf(value) === index);
        
            for(let key of removed_duplicate_keys){
                const array_of_categories = key.split(",");
                html+= "<option value='"+array_of_categories[0]+"'>"+array_of_categories[0]+"</option>";
            }


        html+= "</select>";

        html+= "</div>";
        // لێرە خستوومانەتە ناو درۆپداون چوونکە لە داواکاریەکان واهاتووە
    }
    
    label_html.innerHTML = html;

}



const check_btn = document.getElementById('check-btn');
check_btn.addEventListener('click', function(){
    // دەکەین ئەمانە روودەدەن check لێرە کاتێک کلیک لەسەر 
    const select_labels = document.querySelectorAll(".select-labels");
    // سەرەتا نرخی ئەو درۆپداونانەی کە نووسیبومان دەیانهێنینەوە

    let user_entry = [];
    select_labels.forEach(element => {
        user_entry.push(element.value);
    });
    // لێرە نرخەکانیان دەخەینە ناو ئەم ڤاریەبڵە کە ئەررەیە
   
    // here use the values variable

    calculate_label(values, user_entry);
    // لێرەش بەراوردی دەکەین و حسابی دەکەین
})


function calculate_label(values, user_entry){

    console.log(values, user_entry)

    const copy_required_label = { ...values.required_label };
    // لێرە نرخەکان کۆپی دەکەین بەڵام بەجۆرێک کە رێفرێنسی نەبێت بۆ ئەوەی پێشخۆی، چوونکە کە نرخەکانمان گۆری لەوەی تریش نەگۆرێت

    const keys_required_labels = Object.keys(values.required_label)
    // لێرەتەنها کێیەکانمان وەرگرتووەتەوە

    let result_of_estimates= new Array(keys_required_labels.length).fill(1);
    // لێرە ئەرەیەک دروستدەکەین کە نرخەکانی هەمووی دەکەین بە یەک
    // ئەمکارەدەکەین تاکو ئەو نرخانەی کە دەستماندەکەوێت بزانین کامیان رێژەکەی زۆرترە تاکو ئەو ببێتە وەڵامی هەڵبژێردراو

    for(let row_required_label = 0; row_required_label<keys_required_labels.length; row_required_label++){

        for(let row_prob=0; row_prob<values.prob.length; row_prob++){

            result_of_estimates[row_required_label]*= values.prob[row_prob][user_entry[row_prob]+","+keys_required_labels[row_required_label]];
            console.log(user_entry[row_prob]+","+keys_required_labels[row_required_label], 'are the keys');
            // لێرە تەنها نرخەکان جاران دەکەین وەکو چۆن لە هاوکێشەکە هاتووە تاکو یەک ئەنجاممان بۆ ئەو نرخانەی لە 
            // لەیبڵە داواکراوەکە دەوێت پێمان بڵێت کە کامەیە
        }

    }


    // console.log(result_of_estimates, 'is the result of estimates');

    const sum_of_required_label = Object.values(values.required_label).reduce((acc, value) => acc + value, 0);
    // لێرە کۆکراوەی هەموو لەیبڵە داواکراوەکان دەکەین(لەسەرەوەش کردوومانە)


    for(let key of keys_required_labels){
        copy_required_label[key]= copy_required_label[key]/sum_of_required_label;
    }
    // لێرە ژمارەکان دووبارە حساب دەکەین چوونکە لە جارانەکەی سەرەوە تەنها نرخی لەیبڵی داواکراومان لەگەڵ جاران نەکردبوو

    let loop = 0;
    for(let key of keys_required_labels){
        result_of_estimates[loop]*= copy_required_label[key];
        loop+=1;
    }
    // لێرە ئەو جانەش دەکەین

    // console.log(copy_required_label, ' is the values of calculation');
    console.log(result_of_estimates, 'is the final result');

    const maxNumber = Math.max(...result_of_estimates);
    // لەو نرخانەی کە وەرمانگرت کامیان لە هەمووی گەورەترە

    const indexOfMax = result_of_estimates.indexOf(maxNumber);
    // لێرە ئیندێکسەکەش دەهێنینەوە تاکو بتوانین 

    let loop1=0
    let string = "";
    for(let key of keys_required_labels){
        string = key;
        if(loop1==indexOfMax){
            break;
        }
        loop+=1;
    }
    // لێرەش ئەمانەوێت کێیەکە بهێنینەوە(واتا بە سترینگ) تاکو بتوانین پیشانی بدەینەوە

    console.log(indexOfMax);  // Output: 20

    
    const result = document.getElementById('result-value');
    result.innerHTML = maxNumber+" - "+string
    // لێرەش پیشانمان داوەتەوە

}

    function exportTableToExcel(tableId, filename = ''){
        var downloadLink;
        var dataType = 'application/vnd.ms-excel';
        var tableSelect = document.getElementById(tableId);
        var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');

        // Specify file name
        filename = filename ? filename + '.xls' : 'excel_data.xls';

        // Create download link element
        downloadLink = document.createElement("a");

        document.body.appendChild(downloadLink);

        if(navigator.msSaveOrOpenBlob){
            var blob = new Blob(['\ufeff', tableHTML], {
                type: dataType
            });
            navigator.msSaveOrOpenBlob( blob, filename);
        }else{
            // Create a link to the file
            downloadLink.href = 'data:' + dataType + ', ' + tableHTML;

            // Setting the file name
            downloadLink.download = filename;

            // Triggering the function
            downloadLink.click();
        }
    }