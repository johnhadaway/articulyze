<!DOCTYPE html>
<html lang="en">
<head>
    <title>Chad</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- stylesheets -->
    <link rel="stylesheet" href = "../css/bootstrap.min.css">
    <link rel="stylesheet" href = "../css/bootstrap-grid.css">
    <link rel="stylesheet" href = "../css/art-style.css">
    <link rel="stylesheet" href = "../css/art-country-style.css">
    <link rel="icon" href="../img/ICONS/glass.png">
    <?php
    $db = new PDO("sqlite:current_unocha.db");
    $sql = 'SELECT * FROM chadcountry WHERE days_in_db > (SELECT MAX(days_in_db) FROM chadcountry) - 7 GROUP BY title ORDER BY score DESC';
    $result = $db->query($sql);
    $rowarray = $result->fetchall(PDO::FETCH_ASSOC);
    $x = 0;

    function show($rowarray){
        global $x;
        $title = $rowarray[$x]['title'];
        echo "$title";
    };
    
    function show2($rowarray){
        global $x;
        $url = $rowarray[$x]['url'];
        echo "<a class='art-div-link' href='$url'></a>";       
        $x++;
    }
    ?>
</head>
<body>
    <nav class="navbar navbar-expand navbar-dark fixed-top art-style-back-black">
      <a href="../index.html" class="pull-left"><img src="../img/vertical/navbar.png" width="35px" height="30px"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#art-navbarCollapse" aria-controls="art-navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="art-navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="../countries.html">Countries</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="../about.html">About</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container-fluid chad-div-page">
        <div class="row art-style-10-height"></div>
        <div class="row">
            <div class="col-md-3 col-1"></div>
            <div class="col-md-6 col-10 art-style-back-red art-container-country">
                <p class="text-uppercase country-name-text art-unselectable">Chad</p>
            </div>
            <div class="col-md-3 col-1"></div>
        </div>
        <div class="row art-style-15-height"></div>
        <div class="row">
            <div class="col-md-6 col-2"></div>
            <div class="col-md-5 col-8 art-style-back-red">
                <div class="row art-container-country">
                    <div class="col-12 art-style-white-3-bborder">
                        <p class="text-uppercase art-country-title-style art-unselectable">Summary:</p>
                    </div>
                    <div class="col-12">
                        <p class="art-style-text-white sec-font art-style-margins-country art-unselectable">According to the OCHA, Chad suffers from widespread food insecurity, the proliferation of displaced populations, a public health emergency, and recurring natural disasters. With an estimated 350,000 cases of acute malnutrition in children between the ages of 6 and 59 months, more than 700,000 displaced people, a high prevalence of epidemic-prone diseases, and recurrent floods and droughts, development in Chad has been fraught. Chad ranks 186th in the Human Development Index (2015). </p>
                    </div>
                </div>
            </div>
            <div class="col-md-1 col-2"></div>
        </div>
        <div class="row art-style-10-height"></div>
        <div class="row">
            <div class="col-md-2 col-2"></div>
            <div class="col-md-5 col-8 art-style-back-red">
                <div class="row art-container-country">
                    <p class="text-uppercase art-country-title-style art-unselectable">Articles:</p>
                </div>
                <div class="row">
                    <div class="col-3 art-number-style art-unselectable">1.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">2.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">3.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">4.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">5.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                </div>
            </div>
            <div class="col-md-5 col-2"></div>
        </div>
        <div class="row art-style-20-height"></div>
    </div>
</body>
</html>