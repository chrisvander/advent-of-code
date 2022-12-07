use std::{
    error::Error,
    io::{BufRead, Lines},
};

pub fn solve<F>(lines: &mut Lines<F>) -> Result<String, Box<dyn Error>>
where
    F: Sized + BufRead,
{
    for line in lines {
        dbg!(line?);
    }
    Ok("ans".to_string())
}
