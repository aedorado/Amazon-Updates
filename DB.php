<?php
class DB {
    private static $_instance = null;
    private $_pdo, $_query, $_results;
    private $_error = false;
    private $_count = 0;

    private function __construct() {
        try {
            $this -> _pdo = new PDO('mysql:host=' . Config::get('mysql/host') . ';dbname=' . Config::get('mysql/db') , Config::get('mysql/username'), Config::get('mysql/password'));
            //echo 'connected';
        } catch (PDOException $e) {
            die($e -> getMessage());
        }
    }
    
    public static function getInstance() {
        if (!isset(self::$_instance)) {
            self::$_instance = new DB();
        }
        return self::$_instance;
    }
    
    public function query($sql, $params = array()) {
        $this -> _error = false;
        if ($this -> _query = $this -> _pdo -> prepare($sql)) {   //echo 'Success';

            $x = 1;
            if (count($params)) {
                foreach ($params as $param) {
                    $this->_query->bindValue($x, $param);
                    $x++;
                }
            }
            
            if ($this ->_query->execute()) {
                $this->_results = $this->_query->fetchAll(PDO::FETCH_OBJ);
                $this->_count = $this->_query->rowCount();
            } else {
                $this->_error = true;
            }
        }
        return $this;
    }
    
    public function error() {
        return $this -> _error;
    }
    
    public function action($action, $table, $where = array()) {
        if (count($where) === 3) {
            $operators = array('=', '>', '<', '>=', '<=');
            
            $field = $where[0];
            $operator = $where[1];
            $value = $where[2];
            //echo $field.' '.$operator.' '.$value.nl2br("\n");
            if (in_array($operator, $operators)) {
                //$sql = "SELECT * FROM users WHERE username = ''";
                $sql = "{$action} FROM {$table} WHERE {$field} {$operator} ?";
                //echo $sql;
                if (!($this->query($sql, array($value))->error())) {
                    return $this;
                }
            }
        }
        return $this;
    }
    
    public function results() {
        return $this->_results;
    }
    
    public function first() {
        return $this->_results[0];
        return results()[0];
    }

    public function get($table, $where) {
        return $this->action('SELECT *', $table, $where);
    }
    
    public function delete($table, $where) {
        return $this->action('DELETE', $table, $where);
    }
    
    public function count() {
        return $this->_count;
    }
    
    public function insert($table, $fields = array()) {
        if (count($fields)) {
            $keys = array_keys($fields);
            $values = null;
            $x = 1;
            
            foreach($fields as $field) {
                $values .= '?';
                if ($x < count($fields)) {
                    $values .= ', ';
                }
                $x++;
            }
            
            $sql = "INSERT INTO {$table} (`" . implode('`, `', $keys) . "`) VALUES ({$values})";
            
            if (!$this->query($sql, $fields)->error()) {
                return true;
            }
        }
    }
    
    public function update($table, $id, $fields) {
        $set = '';
        $x = 1;
        
        foreach ($fields as $name => $value) {
            $set .= "{$name} = ?";
            if ($x < count($fields)) {
                $set .= ', ';
            }
            $x++;
        }
        //die ($set);
        $sql = "UPDATE {$table} SET {$set} WHERE id = {$id}";
        //echo $sql;
        if (!$this->query($sql, $fields)->error()) {
                return true;
        }
    }

}

?>

